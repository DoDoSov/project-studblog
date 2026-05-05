<script>
  import Category from '../lib/components/Category.svelte';
  import PostCard from '../lib/components/PostCard.svelte';
  import PostCardSmall from '../lib/components/PostCardSmall.svelte';
  import Promo from '../lib/components/Promo.svelte';
  import { posts as postsApi } from '../lib/api.js';
  import { authStore } from '../lib/store.js';
  import { getSavedSet, toggleSaved, shuffle } from '../lib/utils.js';

  export let onPostClick = () => {};
  export let searchQuery = '';

  let selectedCategory = 'All';
  let allPosts = [];
  let loading = true;
  let fetchError = '';
  let likedSet = new Set();
  let laterSet = new Set();

  async function loadPosts() {
    loading = true; 
    fetchError = '';
    try { 
      allPosts = await postsApi.list(selectedCategory, 100); 
    } catch (err) { 
      fetchError = err.message ?? 'Failed to load posts'; 
    } finally { 
      loading = false; 
    }
  }

  $: if (selectedCategory || searchQuery === '') {
    loadPosts();
  }

  $: {
    const uid = $authStore.user?.id || 'guest';
    likedSet = getSavedSet('liked_posts', uid);
    laterSet = getSavedSet('read_later_posts', uid);
  }

  $: searchedPosts = searchQuery 
    ? allPosts.filter(p => p.title?.toLowerCase().includes(searchQuery.toLowerCase())) 
    : allPosts;

  // UPDATED: Popularity sorting by Likes + Views
  $: popularPosts = [...searchedPosts]
    .sort((a, b) => {
      const scoreA = (a.likes || 0) + (a.views || 0) * 0.1;
      const scoreB = (b.likes || 0) + (b.views || 0) * 0.1;
      return scoreB - scoreA;
    })
    .slice(0, 3);

  $: latestPosts = [...searchedPosts]
    .sort((a, b) => new Date(b.created_at || 0) - new Date(a.created_at || 0))
    .slice(0, 4);

  $: recommendedPosts = shuffle(
    searchedPosts.filter(p => !popularPosts.find(pop => pop.id === p.id))
  ).slice(0, 3);

  function changeCategory(category) {
    selectedCategory = category;
  }

  function save(post) {
    if (!$authStore.isLoggedIn) return alert('Please log in first.');
    toggleSaved('read_later_posts', post.id, $authStore.user.id);
    laterSet = getSavedSet('read_later_posts', $authStore.user.id);
  }

  // UPDATED: Like function with Backend Sync
  async function like(post) {
    if (!$authStore.isLoggedIn) return alert('Please log in first.');
    
    // Toggle local UI
    toggleSaved('liked_posts', post.id, $authStore.user.id);
    likedSet = getSavedSet('liked_posts', $authStore.user.id);

    try {
      // Persist to DB via partial update
      await postsApi.update(post.id, { increment_like: true });
      loadPosts(); // Refresh counts
    } catch (err) {
      console.error("Like sync failed", err);
    }
  }
</script>

<div class="h-32"></div>

<section class="max-w-7xl mx-auto px-6 flex flex-col gap-12 pb-20">
  <div class="glass-panel p-4 rounded-3xl sticky top-24 z-20">
    <Category selected={selectedCategory} onSelect={changeCategory} />
  </div>

  {#if loading}
    <div class="py-20 text-center text-blue-400 animate-pulse">Loading posts from backend…</div>
  {:else if fetchError}
    <div class="glass-panel p-10 text-center text-red-400">
      {fetchError} <br/>
      <button class="mt-4 bg-white/10 px-6 py-2 rounded-full" on:click={loadPosts}>Retry</button>
    </div>
  {:else if searchedPosts.length === 0}
    <div class="py-20 text-center text-white/30 italic">No article names match “{searchQuery}”.</div>
  {:else}
    <!-- Popular Section -->
    <section>
      <div class="flex items-center gap-4 mb-8">
        <h2 class="text-2xl font-bold text-white">Popular</h2>
        <div class="h-px flex-grow bg-white/10"></div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {#each popularPosts as post}
          <PostCard 
            {post} 
            onRead={onPostClick} 
            onSave={save} 
            onLike={like} 
            saved={laterSet.has(String(post.id))} 
            liked={likedSet.has(String(post.id))} 
          />
        {/each}
      </div>
    </section>

    <!-- Latest Section -->
    <section>
      <div class="flex items-center gap-4 mb-8">
        <h2 class="text-2xl font-bold text-white">Latest Posts</h2>
        <div class="h-px flex-grow bg-white/10"></div>
      </div>
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {#each latestPosts as post}
          <PostCardSmall {post} onRead={onPostClick} />
        {/each}
      </div>
    </section>
  {/if}
  <Promo />
</section>

<style>
  .glass-panel {
    background: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }
</style>
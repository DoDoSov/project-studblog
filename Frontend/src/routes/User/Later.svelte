<script>
  import { posts as postsApi } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';
  import PostCard from '../../lib/components/PostCard.svelte';
  import { getSavedSet, toggleSaved } from '../../lib/utils.js';

  // Svelte 4 Props
  export let onPostClick = () => {};

  // Standard Svelte 4 variables (Replaces $state)
  let items = [];
  let loading = false;
  let savedSet = new Set();

  // Reactive statement to load data when login state changes (Replaces $effect)
  $: if ($authStore.isLoggedIn) {
    load();
  } else {
    items = [];
    loading = false;
  }

  async function load() {
    if (!$authStore.isLoggedIn) return;
    
    loading = true;
    try {
      // Get the set of IDs from localStorage utility
      savedSet = getSavedSet('read_later_posts', $authStore.user.id);
      
      // Fetch posts from Flask backend
      const all = await postsApi.list('All', 100);
      
      // Filter for only those in our 'Read Later' set[cite: 1]
      items = all.filter(p => savedSet.has(String(p.id)));
    } catch (err) {
      console.error("Failed to load saved posts:", err);
    } finally {
      loading = false;
    }
  }

  function remove(post) {
    if (!$authStore.isLoggedIn) return;
    
    // Toggle status and refresh local list[cite: 1]
    toggleSaved('read_later_posts', post.id, $authStore.user.id);
    load(); 
  }
</script>

<div class="h-32"></div>

<section class="max-w-7xl mx-auto px-6 pb-20">
  <header class="bg-white/5 p-10 rounded-[3rem] border border-white/10 mb-12">
    <p class="text-[10px] font-black text-emerald-400 tracking-[0.3em] uppercase mb-4">Personal library</p>
    <h1 class="text-5xl font-black text-white">Read Later</h1>
    <p class="text-white/40 mt-4">A curated list of articles you've saved to catch up on later.</p>
  </header>

  {#if !$authStore.isLoggedIn}
    <div class="glass-panel p-20 text-center rounded-[3rem]">
      <h2 class="text-2xl font-bold text-white/40 italic">Please log in to see saved posts.</h2>
    </div>
  {:else if loading}
    <div class="py-20 text-center text-emerald-400 animate-pulse font-medium">Retrieving your reading list...</div>
  {:else if items.length === 0}
    <div class="glass-panel p-20 text-center rounded-[3rem]">
      <h2 class="text-2xl font-bold text-white/20 italic">No saved posts yet.</h2>
      <p class="text-white/10 mt-2">Bookmark interesting articles to see them appear here.</p>
    </div>
  {:else}
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {#each items as post}
        <PostCard 
          {post} 
          onRead={onPostClick} 
          onSave={remove} 
          saved={true}
        />
      {/each}
    </div>
  {/if}
</section>

<style>
  /* Tailwind 4.0 Glass Effect consistency[cite: 1] */
  .glass-panel {
    background-color: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }
</style>
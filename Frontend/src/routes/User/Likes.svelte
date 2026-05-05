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
  let likedSet = new Set();

  // Reactive trigger: Reload when login status changes (Replaces $effect)
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
      likedSet = getSavedSet('liked_posts', $authStore.user.id);
      
      // Fetch posts from Flask backend
      const all = await postsApi.list('All', 100);
      
      // Filter for only those in our liked set
      items = all.filter(p => likedSet.has(String(p.id)));
    } catch (err) {
      console.error("Failed to load liked posts:", err);
    } finally {
      loading = false;
    }
  }

  function unlike(post) {
    if (!$authStore.isLoggedIn) return;
    
    // Toggle status and refresh local list[cite: 1]
    toggleSaved('liked_posts', post.id, $authStore.user.id);
    load(); 
  }
</script>

<div class="h-32"></div>

<section class="max-w-7xl mx-auto px-6 pb-20">
  <header class="bg-white/5 p-10 rounded-[3rem] border border-white/10 mb-12">
    <p class="text-[10px] font-black text-blue-400 tracking-[0.3em] uppercase mb-4">Personal library</p>
    <h1 class="text-5xl font-black text-white">Liked Posts</h1>
    <p class="text-white/40 mt-4">Articles you've marked as favorites for quick access.</p>
  </header>

  {#if !$authStore.isLoggedIn}
    <div class="glass-panel p-20 text-center rounded-[3rem]">
      <h2 class="text-2xl font-bold text-white/40 italic">Please log in to see liked posts.</h2>
    </div>
  {:else if loading}
    <div class="py-20 text-center text-blue-400 animate-pulse font-medium">Fetching your favorites...</div>
  {:else if items.length === 0}
    <div class="glass-panel p-20 text-center rounded-[3rem]">
      <h2 class="text-2xl font-bold text-white/20 italic">No liked posts yet.</h2>
      <p class="text-white/10 mt-2">Explore the home feed to find content you love.</p>
    </div>
  {:else}
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {#each items as post}
        <PostCard 
          {post} 
          onRead={onPostClick} 
          onLike={unlike} 
          liked={true}
        />
      {/each}
    </div>
  {/if}
</section>

<style>
  /* Tailwind 4.0 Glass Effect matching your theme[cite: 1] */
  .glass-panel {
    background-color: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }
</style>
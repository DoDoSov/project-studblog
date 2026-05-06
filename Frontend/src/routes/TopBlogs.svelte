<script>
  import { onMount } from 'svelte';
  import { posts as postsApi } from '../lib/api.js';
  import PostCard from '../lib/components/PostCard.svelte';
  import { CATEGORIES } from '../lib/utils.js';

  export let onPostClick = () => {};

  let posts = [];
  let loading = true;
  let error = '';
  let activeTab = 'All'; 

  onMount(() => {
    load();
  });

  async function load() {
    loading = true;
    error = '';
    try {
      // Fetching everything (null category) once to populate the "Trending" pool
      const response = await postsApi.list(null, 100);
      posts = response || [];
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  // Logic to find "Popular" posts for a specific category locally from the pool
  function getTopPosts(cat, limit = 9) {
    let filtered = posts;
    
    if (cat !== 'All') {
      filtered = posts.filter(p => p.category === cat);
    }

    return filtered
      .sort((a, b) => {
        // Engagement Score Calculation
        const scoreA = (a.likes || 0) * 10 + (a.views || 0);
        const scoreB = (b.likes || 0) * 10 + (b.views || 0);
        if (scoreB !== scoreA) return scoreB - scoreA;
        // Secondary Sort: Newest first
        return new Date(b.created_at) - new Date(a.created_at);
      })
      .slice(0, limit);
  }

  // Only show categories in the selection bar that actually have content
  $: availableCategories = CATEGORIES.filter(c => 
    c === 'All' || posts.some(p => p.category === c)
  );

  // Reactively calculate which posts to show based on the active tab
  $: displayPosts = getTopPosts(activeTab, 9);
</script>

<div class="h-32"></div>

<section class="max-w-7xl mx-auto px-6 flex flex-col gap-8 pb-20">
  <header class="bg-gradient-to-br from-blue-600/20 to-purple-600/20 p-10 rounded-[3rem] border border-white/10 relative overflow-hidden">
    <div class="absolute top-0 right-0 -mt-10 -mr-10 w-40 h-40 bg-blue-500/10 blur-[80px] rounded-full"></div>
    
    <p class="text-blue-400 font-bold uppercase tracking-widest text-xs mb-4 flex items-center gap-2">
      <span class="inline-block w-2 h-2 bg-blue-400 rounded-full animate-pulse"></span>
      Trending Content
    </p>
    <h1 class="text-5xl font-black text-white leading-tight mb-4">Popular by Category</h1>
    <p class="text-white/40  self-center">
      Explore the community's favorite picks. Use the topics below to filter the highest-rated discussions.
    </p>
  </header>

  <!-- Topic Selection Bar -->
  <div class="flex flex-wrap gap-3 items-center border-b border-white/5 pb-6">
    <span class="text-white/30 text-xs font-bold uppercase tracking-tighter mr-2">Hot Topics:</span>
    {#each availableCategories as cat}
      <button 
        on:click={() => activeTab = cat}
        class="px-5 py-2 rounded-full text-sm font-bold transition-all border
        {activeTab === cat 
          ? 'bg-blue-600 border-blue-500 text-white shadow-[0_0_20px_rgba(37,99,235,0.3)]' 
          : 'bg-white/5 border-white/10 text-white/50 hover:bg-white/10 hover:text-white'}"
      >
        {cat}
      </button>
    {/each}
  </div>

  {#if loading}
    <div class="py-20 text-center flex flex-col items-center gap-4">
      <div class="w-12 h-12 border-4 border-blue-500/20 border-t-blue-500 rounded-full animate-spin"></div>
      <p class="text-blue-400 font-medium">Analyzing engagement trends…</p>
    </div>
  {:else if error}
    <div class="glass-panel p-10 text-center text-red-400 border-red-500/20 rounded-2xl">{error}</div>
  {:else if posts.length === 0}
    <div class="py-20 text-center text-white/20 italic bg-white/5 rounded-3xl border border-dashed border-white/10">
      No posts found in the database. Start writing to see rankings!
    </div>
  {:else}
    <div class="space-y-8">
      <div class="flex items-center gap-4">
        <h2 class="text-2xl font-bold text-white flex items-center gap-3">
          {activeTab} <span class="text-xs font-normal text-white/30 uppercase">Top Rated</span>
        </h2>
        <div class="h-px flex-grow bg-gradient-to-r from-white/10 to-transparent"></div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {#each displayPosts as post (post.id)}
          <div class="relative group">
            {#if (post.likes > 0)}
              <div class="absolute -top-3 -right-3 z-10 bg-blue-600 text-white text-[10px] font-bold px-2 py-1 rounded shadow-lg">
                🔥 {post.likes} LIKES
              </div>
            {/if}
            <PostCard {post} onRead={() => onPostClick(post)} />
          </div>
        {/each}
      </div>
    </div>
  {/if}
</section>

<style>
  .glass-panel {
    background: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }
</style>
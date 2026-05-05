<script>
  import { untrack } from 'svelte';
  import Category from '../lib/components/Category.svelte';
  import PostCard from '../lib/components/PostCard.svelte';
  import PostCardSmall from '../lib/components/PostCardSmall.svelte';
  import Promo from '../lib/components/Promo.svelte';
  import { posts as postsApi } from '../lib/api.js';

  let { onPostClick } = $props();

  // --- Svelte 5 State Runes ---
  let selectedCategory = $state('All');
  let allPosts = $state([]);
  let loading = $state(true);
  let fetchError = $state('');

  async function loadPosts() {
    loading = true;
    fetchError = '';
    try {
      // Requesting 50 to ensure we have enough to slice into sections
      const data = await postsApi.list(selectedCategory, 50);
      allPosts = Array.isArray(data) ? data : [];
    } catch (err) {
      console.error("Fetch Error:", err);
      fetchError = err.message ?? 'Failed to load posts';
    } finally {
      loading = false;
    }
  }

  // Effect: Only re-run when category changes, ignoring other state updates
  $effect(() => {
    selectedCategory; // Dependent on category
    untrack(() => {
      loadPosts();
    });
  });
  function handleCategoryChange(category) {
    selectedCategory = category;
  }
  // Improved Reactive sections
  let trendingPosts = $derived(allPosts.slice(0, 3));
  
  // Latest will now show whatever is left after trending, up to 3 posts
  let latestPosts = $derived(allPosts.length > 3 ? allPosts.slice(3, 6) : []);
  
  // Discovery will show everything after Trending and Latest
  let morePosts = $derived(allPosts.length > 6 ? allPosts.slice(6) : []);
</script>

<!-- Spacer for fixed Nav -->
<div class="h-32"></div>

<div class="max-w-7xl mx-auto px-4 md:px-6 flex flex-col gap-10 pb-20 text-white font-sans relative z-10">
  
  <!-- Category Bar with Glass Style from image_3c43f9.png -->
  <div class="glass-panel p-4 rounded-3xl sticky top-24 z-20">
    <Category onSelect={handleCategoryChange} />
  </div>

  {#if loading}
    <div class="flex flex-col items-center justify-center py-40 gap-6">
      <div class="relative size-16">
        <div class="absolute inset-0 border-4 border-blue-500/20 rounded-full"></div>
        <div class="absolute inset-0 border-4 border-blue-400 border-t-transparent rounded-full animate-spin"></div>
      </div>
      <p class="text-blue-400/80 font-medium tracking-[0.1em] animate-pulse">Syncing with Gemini...</p>
    </div>
  {:else if fetchError}
    <div class="glass-panel text-center py-16 border-red-500/20 bg-red-500/5">
      <p class="text-red-400 font-medium">{fetchError}</p>
      <button onclick={loadPosts} class="mt-6 px-6 py-2 bg-white/5 hover:bg-white/10 rounded-full text-xs uppercase tracking-widest transition-all">
        Try Reconnecting
      </button>
    </div>
  {:else}

    <!-- Trending Section -->
    <section class="glass-panel p-8 rounded-[2.5rem]">
      <div class="flex items-center gap-4 mb-8">
        <div class="size-2 rounded-full bg-blue-400 shadow-[0_0_10px_#60a5fa]"></div>
        <h2 class="text-xs font-black text-blue-400 uppercase tracking-[0.2em]">Trending</h2>
        <div class="h-[1px] flex-grow bg-gradient-to-r from-blue-400/20 to-transparent"></div>
        <span class="text-[10px] font-bold text-white/20 uppercase tracking-widest">{selectedCategory}</span>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each trendingPosts as post}
          <div class="hover:scale-[1.01] transition-transform duration-500">
            <PostCard {...post} onRead={() => onPostClick?.(post)} />
          </div>
        {:else}
          <p class="col-span-full text-center py-10 text-white/20 italic">No cosmic data found in this sector.</p>
        {/each}
      </div>
    </section>

    <!-- Latest Section -->
    {#if latestPosts.length > 0}
    <section class="glass-panel p-8 rounded-[2.5rem]">
      <div class="flex items-center gap-4 mb-8">
        <div class="size-2 rounded-full bg-purple-400 shadow-[0_0_10px_#c084fc]"></div>
        <h2 class="text-xs font-black text-purple-400 uppercase tracking-[0.2em]">Latest</h2>
        <div class="h-[1px] flex-grow bg-gradient-to-r from-purple-400/20 to-transparent"></div>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each latestPosts as post}
          <div class="hover:scale-[1.01] transition-transform duration-500">
            <PostCard {...post} onRead={() => onPostClick?.(post)} />
          </div>
        {/each}
      </div>
    </section>
    {/if}

    <!-- Discovery Section (PostCardSmall) -->
    {#if morePosts.length > 0}
      <section class="glass-panel p-8 rounded-[2.5rem]">
        <div class="flex items-center gap-4 mb-8">
          <div class="size-2 rounded-full bg-emerald-400 shadow-[0_0_10px_#34d399]"></div>
          <h2 class="text-xs font-black text-emerald-400 uppercase tracking-[0.2em]">Discovery</h2>
          <div class="h-[1px] flex-grow bg-gradient-to-r from-emerald-400/20 to-transparent"></div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {#each morePosts as post}
            <PostCardSmall {...post} />
          {/each}
        </div>
      </section>
    {/if}

  {/if}

  <Promo />
</div>

<style>
  .glass-panel {
    background: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7);
  }
</style>
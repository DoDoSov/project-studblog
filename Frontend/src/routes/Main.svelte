<script>
  import Category from '../lib/components/Category.svelte';
  import PostCard from '../lib/components/PostCard.svelte';
  import PostCardSmall from '../lib/components/PostCardSmall.svelte';
  import Promo from '../lib/components/Promo.svelte';
  import { posts as postsApi } from '../lib/api.js';

  let { onPostClick } = $props();

  let selectedCategory = $state('All');
  let allPosts   = $state([]);
  let loading    = $state(true);
  let fetchError = $state('');

  async function loadPosts() {
    loading    = true;
    fetchError = '';
    try {
      allPosts = await postsApi.list(selectedCategory);
    } catch (err) {
      fetchError = err.message ?? 'Failed to load posts';
    } finally {
      loading = false;
    }
  }

  $effect(() => {
    loadPosts();
  });

  // Split posts into display sections by index since there's no `type` field
  let trendingPosts = $derived(allPosts.slice(0, 3));
  let latestPosts   = $derived(allPosts.slice(3, 6));
  let morePosts     = $derived(allPosts.slice(6));

  function handleCategoryChange(category) {
    selectedCategory = category;
  }
</script>

<div class="h-32"></div>

<div class="bg-[#1b2236] rounded-2xl max-w-7xl mx-auto px-4 md:px-6 flex flex-col gap-12 pb-20 text-white font-sans">
  <div class="h-4"></div>
  <Category onSelect={handleCategoryChange} />

  {#if loading}
    <div class="flex justify-center py-20">
      <div class="size-10 border-2 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
    </div>
  {:else if fetchError}
    <div class="text-center py-16 text-red-400">{fetchError}</div>
  {:else}

    <section class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl">
      <div class="flex items-center gap-4 mb-8">
        <h2 class="text-sm font-black text-blue-400 uppercase tracking-widest">Trending</h2>
        <div class="h-[1px] flex-grow bg-white/5"></div>
        <span class="text-[10px] font-bold text-gray-500 uppercase">{selectedCategory}</span>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each trendingPosts as post}
          <PostCard {...post} onRead={() => onPostClick?.(post)} />
        {:else}
          <p class="col-span-full text-center py-10 text-gray-500 italic">No trending posts yet.</p>
        {/each}
      </div>
    </section>

    <section class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl">
      <div class="flex items-center gap-4 mb-8">
        <h2 class="text-sm font-black text-purple-400 uppercase tracking-widest">Latest</h2>
        <div class="h-[1px] flex-grow bg-white/5"></div>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {#each latestPosts as post}
          <PostCard {...post} onRead={() => onPostClick?.(post)} />
        {:else}
          <p class="col-span-full text-center py-10 text-gray-500 italic">No new posts yet.</p>
        {/each}
      </div>
    </section>

    {#if morePosts.length > 0}
    <section class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl">
      <div class="flex items-center gap-4 mb-8">
        <h2 class="text-sm font-black text-green-400 uppercase tracking-widest">Discovery</h2>
        <div class="h-[1px] flex-grow bg-white/5"></div>
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

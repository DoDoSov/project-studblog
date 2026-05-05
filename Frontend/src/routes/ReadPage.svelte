<script>
  import { posts as postsApi } from '../lib/api.js';
  import { authStore } from '../lib/store.js';
  import PostCardSmall from '../lib/components/PostCardSmall.svelte';
  import { 
    imageFor, 
    formatDate, 
    readTime, 
    getSavedSet, 
    toggleSaved, 
    shuffle 
  } from '../lib/utils.js';

  // Svelte 4 Props
  export let post = null;
  export let onPostClick = () => {};

  let similar = [];
  let shareOpen = false;
  let copied = false;
  let liked = false;
  let saved = false;
  let lastRead = null;

  // Svelte 4 Reactive Declarations
  $: shareUrl = post?.id ? `${window.location.origin}${window.location.pathname}#post-${post.id}` : window.location.href;
  $: embedCode = post?.id ? `<iframe src="${shareUrl}" title="${post.title}" width="800" height="600"></iframe>` : '';

  // Watch for post changes
  $: if (post && post.id) {
    updatePostContext(post);
  } else if ($authStore.user?.id) {
    try { 
      lastRead = JSON.parse(localStorage.getItem(`last_read_${$authStore.user.id}`)); 
    } catch { 
      lastRead = null; 
    }
  }

  function updatePostContext(p) {
    const tones = ['dark', 'warm', 'green'];
    document.documentElement.dataset.theme = tones[Number(p.id) % tones.length];
    
    loadSimilar(p);
    
    const uid = $authStore.user?.id;
    if (uid) {
      localStorage.setItem(`last_read_${uid}`, JSON.stringify(p));
      lastRead = p;
      liked = getSavedSet('liked_posts', uid).has(String(p.id));
      saved = getSavedSet('read_later_posts', uid).has(String(p.id));
    }
  }

  async function loadSimilar(base) {
    try {
      const data = await postsApi.list(base.category, 50);
      similar = shuffle(data.filter(item => item.id !== base.id)).slice(0, 4);
    } catch (err) {
      console.error("Failed to load similar posts:", err);
      similar = [];
    }
  }

  function toggleLike() {
    if (!$authStore.isLoggedIn) return alert('Please log in first.');
    liked = toggleSaved('liked_posts', post.id, $authStore.user.id);
  }

  function toggleLater() {
    if (!$authStore.isLoggedIn) return alert('Please log in first.');
    saved = toggleSaved('read_later_posts', post.id, $authStore.user.id);
  }

  async function copy(text) {
    try {
      await navigator.clipboard.writeText(text);
      copied = true;
      setTimeout(() => copied = false, 1200);
    } catch (err) {
      console.error("Copy failed", err);
    }
  }
</script>

<div class="h-32"></div>

<section class="max-w-7xl mx-auto px-6 grid grid-cols-1 lg:grid-cols-3 gap-12 pb-20">
  {#if post}
    <article class="lg:col-span-2 space-y-8">
      <div class="rounded-[3rem] overflow-hidden border border-white/10 shadow-2xl">
        <img 
          class="w-full aspect-video object-cover" 
          src={post.banner_url || imageFor(post)} 
          alt={post.title} 
        />
      </div>

      <div class="space-y-6">
        <p class="text-blue-400 font-bold text-xs uppercase tracking-widest">
          {post.category} • {formatDate(post.created_at)} • {readTime(post.content)}
        </p>
        
        <h1 class="text-4xl md:text-6xl font-black text-white leading-tight">
          {post.title}
        </h1>
        
        <p class="text-xl text-white/60 italic leading-relaxed">
          {post.description}
        </p>

        <div class="flex flex-wrap gap-4 pt-4">
          <button class="bg-blue-600 hover:bg-blue-500 text-white px-8 py-3 rounded-full font-bold transition-all" on:click={toggleLike}>
            {liked ? 'Liked ♥' : 'Like ♥'}
          </button>
          <button class="bg-white/10 hover:bg-white/20 text-white px-8 py-3 rounded-full font-bold transition-all" on:click={toggleLater}>
            {saved ? 'Saved ✓' : 'Read Later 🔖'}
          </button>
          <button class="bg-white/5 hover:bg-white/10 text-white px-8 py-3 rounded-full font-bold transition-all border border-white/10" on:click={() => shareOpen = true}>
            Share
          </button>
        </div>
      </div>

      <!-- RICH HTML CONTENT RENDERING -->
      <div class="rich-content border-t border-white/5 pt-10">
        {@html post.content}
      </div>
    </article>
  {:else}
    <div class="lg:col-span-2 py-40 text-center space-y-6 glass-panel rounded-[3rem]">
      <h2 class="text-3xl font-bold text-white/40">No post selected</h2>
      {#if $authStore.isLoggedIn && lastRead}
        <p class="text-white/20">Your last read post was:</p>
        <div class="max-w-md mx-auto">
          <PostCardSmall post={lastRead} onRead={onPostClick} />
        </div>
      {:else}
        <p class="text-white/20">Choose an article from Home or Top Blogs to begin.</p>
      {/if}
    </div>
  {/if}

  <aside class="space-y-10">
    {#if $authStore.isLoggedIn && lastRead}
      <div class="glass-panel p-8 rounded-[2.5rem] space-y-6">
        <h3 class="text-xs font-black uppercase tracking-[0.2em] text-blue-400">Last read</h3>
        <PostCardSmall post={lastRead} onRead={onPostClick} />
      </div>
    {/if}

    <div class="glass-panel p-8 rounded-[2.5rem] space-y-6">
      <h3 class="text-xs font-black uppercase tracking-[0.2em] text-purple-400">Similar posts</h3>
      <div class="space-y-4">
        {#each similar as item}
          <PostCardSmall post={item} onRead={onPostClick} />
        {:else}
          <p class="text-white/20 italic text-sm">Searching the galaxy for similar content...</p>
        {/each}
      </div>
    </div>
  </aside>
</section>

<!-- Share Modal -->
{#if shareOpen}
  <div class="fixed inset-0 z-[100] flex items-center justify-center p-6 bg-black/80 backdrop-blur-sm" on:click={() => shareOpen = false}>
    <div class="bg-slate-900 border border-white/10 p-8 rounded-[2.5rem] max-w-lg w-full space-y-6 shadow-2xl" on:click|stopPropagation>
      <div class="flex justify-between items-center">
        <h2 class="text-2xl font-bold text-white">Share this post</h2>
        <button class="text-white/40 hover:text-white text-3xl" on:click={() => shareOpen = false}>×</button>
      </div>
      
      <div class="space-y-2">
        <label class="text-xs font-bold text-white/40 uppercase tracking-widest">Direct link</label>
        <div class="flex gap-2">
          <input readonly value={shareUrl} class="flex-grow bg-white/5 border border-white/10 rounded-xl px-4 py-2 text-white/60 text-sm focus:outline-none" />
          <button class="bg-blue-600 px-4 py-2 rounded-xl text-white font-bold text-sm" on:click={() => copy(shareUrl)}>Copy</button>
        </div>
      </div>

      <div class="space-y-2">
        <label class="text-xs font-bold text-white/40 uppercase tracking-widest">HTML Insert</label>
        <textarea readonly rows="4" class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2 text-white/60 text-sm focus:outline-none resize-none">{embedCode}</textarea>
        <button class="w-full bg-white/10 hover:bg-white/20 py-3 rounded-xl text-white font-bold text-sm border border-white/10 transition-all" on:click={() => copy(embedCode)}>Copy HTML</button>
      </div>

      {#if copied}
        <p class="text-center text-emerald-400 font-bold text-sm animate-pulse">Copied to clipboard!</p>
      {/if}
    </div>
  </div>
{/if}

<style>
  .glass-panel {
    background: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }

  /* STYLING FOR INJECTED HTML CONTENT */
  .rich-content {
    color: rgba(255, 255, 255, 0.8);
    font-size: 1.125rem;
    line-height: 1.75;
  }

  /* Using :global because the elements are injected via {@html} */
  .rich-content :global(p) {
    margin-bottom: 1.5rem;
  }

  .rich-content :global(h2), .rich-content :global(h3) {
    color: white;
    font-weight: 800;
    margin-top: 2.5rem;
    margin-bottom: 1rem;
  }

  .rich-content :global(h2) { font-size: 2rem; }
  .rich-content :global(h3) { font-size: 1.5rem; }

  .rich-content :global(img) {
    width: 100%;
    border-radius: 1.5rem;
    margin: 2rem 0;
    border: 1px solid rgba(255, 255, 255, 0.1);
  }

  .rich-content :global(pre) {
    background: #0f1117;
    padding: 1.5rem;
    border-radius: 1rem;
    overflow-x: auto;
    border: 1px solid rgba(255, 255, 255, 0.05);
    margin: 2rem 0;
  }

  .rich-content :global(code) {
    font-family: 'Fira Code', monospace;
    color: #93c5fd;
    font-size: 0.9em;
  }

  .rich-content :global(a) {
    color: #60a5fa;
    text-decoration: underline;
    transition: opacity 0.2s;
  }

  .rich-content :global(a:hover) {
    opacity: 0.8;
  }
</style>
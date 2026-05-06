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

  // --- UPDATED: GITHUB DATA LOGIC ---
  // We no longer fetch from GitHub API; we use the data stored in our DB.
  // We still clean the content to remove the [github: handle/repo] tag for display.
  let cleanContent = '';

  $: if (post && post.content) {
    // Remove the tag from the HTML so it doesn't show as raw text to the reader
    cleanContent = post.content.replace(/<p>\[github:\s*.*?\]<\/p>/g, '').replace(/\[github:\s*.*?\]/g, '');
  }

  // Svelte 4 Reactive Declarations
  $: shareUrl = post?.id 
    ? `${window.location.origin}/#/post/${post.id}` 
    : window.location.href;

  $: embedCode = post?.id ? `<iframe src="${shareUrl}" title="${post.title}" width="800" height="600"></iframe>` : '';
  
  $: qrCodeUrl = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(shareUrl)}&bgcolor=0f172a&color=ffffff`;

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

      <div class="rich-content border-t border-white/5 pt-10">
        {@html cleanContent}
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

    <!-- UPDATED GITHUB SIDEBAR: Pulling from Database Columns -->
    {#if post && post.github_repo}
      <div class="glass-panel p-8 rounded-[2.5rem] space-y-6 border border-white/10 relative overflow-hidden group">
        <div class="relative z-10">
          <h3 class="text-xs font-black uppercase tracking-[0.2em] text-emerald-400 mb-4 flex items-center gap-2">
            <svg height="16" viewBox="0 0 16 16" width="16" fill="currentColor"><path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path></svg>
            Project Repository
          </h3>
          
          <div class="space-y-4">
            <div>
              <p class="text-white font-bold text-sm truncate">{post.github_repo}</p>
              {#if post.last_sync}
                <p class="text-[10px] text-white/30 uppercase font-black">
                  Synced: {formatDate(post.last_sync)}
                </p>
              {/if}
            </div>

            <div class="flex gap-4 border-y border-white/5 py-4">
              <div class="text-center flex-1">
                <span class="block text-xl font-black text-white">{post.github_stars || 0}</span>
                <span class="text-[9px] text-white/40 uppercase tracking-widest font-bold">Stars</span>
              </div>
              <div class="w-px bg-white/5"></div>
              <div class="text-center flex-1">
                <span class="block text-xl font-black text-white">{post.github_forks || 0}</span>
                <span class="text-[9px] text-white/40 uppercase tracking-widest font-bold">Forks</span>
              </div>
            </div>

            <a 
              href="https://github.com/{post.github_repo}" 
              target="_blank" 
              rel="noreferrer"
              class="block w-full py-3 bg-white text-black text-center rounded-xl font-black text-[10px] uppercase tracking-widest hover:bg-emerald-400 transition-colors"
            >
              View Source Code
            </a>
          </div>
        </div>
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
    <div class="bg-slate-900 border border-white/10 p-8 rounded-[2.5rem] max-w-lg w-full space-y-6 shadow-2xl overflow-y-auto max-h-[90vh]" on:click|stopPropagation>
      <div class="flex justify-between items-center">
        <h2 class="text-2xl font-bold text-white uppercase tracking-tighter">Share this post</h2>
        <button class="text-white/40 hover:text-white text-3xl" on:click={() => shareOpen = false}>×</button>
      </div>
      
      <div class="space-y-2">
        <label class="text-[10px] font-black text-white/40 uppercase tracking-[0.2em]">Direct link</label>
        <div class="flex gap-2">
          <input readonly value={shareUrl} class="flex-grow bg-white/5 border border-white/10 rounded-xl px-4 py-2 text-white/60 text-sm focus:outline-none" />
          <button class="bg-blue-600 px-4 py-2 rounded-xl text-white font-bold text-sm" on:click={() => copy(shareUrl)}>Copy</button>
        </div>
      </div>

      <div class="space-y-2">
        <label class="text-[10px] font-black text-white/40 uppercase tracking-[0.2em]">HTML Insert</label>
        <textarea readonly rows="2" class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-2 text-white/60 text-sm focus:outline-none resize-none">{embedCode}</textarea>
        <button class="w-full bg-white/10 hover:bg-white/20 py-3 rounded-xl text-white font-bold text-sm border border-white/10 transition-all" on:click={() => copy(embedCode)}>Copy HTML</button>
      </div>

      <div class="pt-6 border-t border-white/5 text-center space-y-4">
        <label class="text-[10px] font-black text-blue-400 uppercase tracking-[0.2em] block">Scan to Share on Mobile</label>
        <div class="inline-block p-4 bg-white rounded-3xl shadow-xl shadow-blue-500/10">
          <img src={qrCodeUrl} alt="QR Code" class="w-40 h-40" />
        </div>
        <div class="flex gap-2 justify-center">
          <a href={qrCodeUrl} download="qrcode.png" target="_blank" class="text-[10px] font-black text-white/30 uppercase hover:text-white transition-colors">Download QR</a>
          <span class="text-white/10">•</span>
          <button on:click={() => copy(qrCodeUrl)} class="text-[10px] font-black text-white/30 uppercase hover:text-white transition-colors">Copy QR Link</button>
        </div>
      </div>

      {#if copied}
        <p class="text-center text-emerald-400 font-bold text-sm animate-pulse pt-2">Copied to clipboard!</p>
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

  .rich-content {
    color: rgba(255, 255, 255, 0.8);
    font-size: 1.125rem;
    line-height: 1.75;
  }

  .rich-content :global(p) { margin-bottom: 1.5rem; }
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
  .rich-content :global(a:hover) { opacity: 0.8; }
</style>
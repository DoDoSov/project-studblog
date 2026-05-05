<script>
  import { posts as postsApi } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';

  let myPosts    = $state([]);
  let loading    = $state(true);
  let fetchError = $state('');

  // Create-post form state
  let showForm    = $state(false);
  let formTitle   = $state('');
  let formCat     = $state('Technology');
  let formDesc    = $state('');
  let formContent = $state('');
  let saving      = $state(false);
  let saveError   = $state('');

  const CATEGORIES = ['Technology', 'Science', 'Finance', 'Health', 'AI', 'General'];

  async function loadMyPosts() {
    loading    = true;
    fetchError = '';
    try {
      myPosts = await postsApi.mine();
    } catch (err) {
      fetchError = err.message ?? 'Failed to load posts';
    } finally {
      loading = false;
    }
  }

  $effect(() => {
    if (authStore.isLoggedIn) loadMyPosts();
    else loading = false;
  });

  async function handleCreate() {
    saveError = '';
    saving    = true;
    try {
      await postsApi.create({
        title:       formTitle,
        category:    formCat,
        description: formDesc,
        content:     formContent
      });
      formTitle = formDesc = formContent = '';
      showForm  = false;
      await loadMyPosts();
    } catch (err) {
      saveError = err.data?.msg ?? err.message ?? 'Failed to create post';
    } finally {
      saving = false;
    }
  }

  async function handleDelete(id) {
    if (!confirm('Delete this post?')) return;
    try {
      await postsApi.remove(id);
      await loadMyPosts();
    } catch (err) {
      alert(err.data?.msg ?? 'Delete failed');
    }
  }

  function formatDate(iso) {
    if (!iso) return '';
    return new Date(iso).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
  }
</script>

<div class="h-32"></div>

<section class="max-w-7xl bg-[#283047] rounded-2xl mx-auto px-6 mb-20 animate-in fade-in slide-in-from-bottom-6 duration-700">
  <div class="h-4"></div>

  {#if !authStore.isLoggedIn}
    <div class="py-20 text-center text-gray-400">Please log in to manage your posts.</div>
  {:else}

  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-10">
    <div class="lg:col-span-2 bg-[#1A1F2E] p-10 rounded-[2.5rem] border border-white/5 shadow-2xl flex flex-col justify-center relative overflow-hidden">
      <div class="relative z-10">
        <p class="text-[10px] font-black text-blue-400 tracking-[0.2em] uppercase mb-4">Creator Studio</p>
        <h1 class="text-4xl font-bold text-white mb-4">Your Stories</h1>
        <p class="text-gray-400 max-w-md">Manage your drafts, view analytics, and share your knowledge with the student community.</p>
      </div>
      <span class="absolute -right-4 -bottom-10 text-[180px] opacity-5 pointer-events-none">Write</span>
    </div>

    <button
      onclick={() => showForm = !showForm}
      class="bg-blue-600 hover:bg-blue-500 transition-all rounded-[2.5rem] flex flex-col items-center justify-center p-10 group cursor-pointer shadow-xl shadow-purple-900/20"
    >
      <div class="size-16 bg-white/20 rounded-2xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
        <span class="text-3xl text-white">{showForm ? '×' : '+'}</span>
      </div>
      <span class="text-xl font-bold text-white">{showForm ? 'Cancel' : 'Create New Post'}</span>
    </button>
  </div>

  {#if showForm}
  <div class="bg-[#1A1F2E] rounded-[2.5rem] border border-white/5 p-8 mb-8">
    <h2 class="text-lg font-bold text-white mb-6">New Post</h2>
    {#if saveError}
      <div class="mb-4 px-4 py-3 rounded-xl bg-red-500/20 border border-red-500/30 text-red-400 text-sm">{saveError}</div>
    {/if}
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
      <input bind:value={formTitle} placeholder="Title" class="bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50" />
      <select bind:value={formCat} class="bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50">
        {#each CATEGORIES as c}<option value={c}>{c}</option>{/each}
      </select>
    </div>
    <input bind:value={formDesc} placeholder="Short description" class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50 mb-4" />
    <textarea bind:value={formContent} placeholder="Write your post content here…" rows="6" class="w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50 mb-4 resize-none"></textarea>
    <button onclick={handleCreate} disabled={saving || !formTitle || !formContent} class="px-8 py-3 bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white rounded-xl text-sm font-bold transition-all active:scale-95">
      {saving ? 'Publishing…' : 'Publish Post'}
    </button>
  </div>
  {/if}

  <div class="bg-[#1A1F2E] rounded-[2.5rem] border border-white/5 overflow-hidden shadow-2xl">
    <div class="p-8 border-b border-white/5 bg-white/5 flex justify-between items-center">
      <h2 class="font-bold text-white">Active Manuscripts</h2>
      <span class="px-3 py-1 bg-black/20 rounded-full text-[10px] font-bold text-gray-400 uppercase tracking-widest border border-white/5">
        Total: {myPosts.length}
      </span>
    </div>

    {#if loading}
      <div class="p-12 flex justify-center">
        <div class="size-8 border-2 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
      </div>
    {:else if fetchError}
      <div class="p-12 text-center text-red-400">{fetchError}</div>
    {:else if myPosts.length === 0}
      <div class="p-12 text-center text-gray-500 italic">No posts yet. Create your first one!</div>
    {:else}
      <div class="divide-y divide-white/5">
        {#each myPosts as post}
          <div class="p-6 hover:bg-white/[0.02] transition-colors flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div class="flex flex-col gap-1">
              <span class="text-sm font-bold text-white">{post.title}</span>
              <p class="text-[10px] text-gray-500 font-medium">{formatDate(post.created_at)} • {post.category}</p>
            </div>
            <div class="flex items-center gap-2">
              <button
                onclick={() => handleDelete(post.id)}
                class="p-3 bg-red-500/10 hover:bg-red-500/20 rounded-xl transition-all border border-red-500/10 text-red-400 text-xs font-bold"
              >Delete</button>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>

  {/if}
  <div class="h-4"></div>
</section>

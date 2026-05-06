<script>
  import { onMount } from 'svelte';
  import { admin as adminApi, posts as postsApi } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';

  // ── State ──────────────────────────────────────────────────────────────────
  let activeTab = 'pending'; // 'pending' | 'all'
  let pendingPosts = [];
  let allPosts = [];
  let loading = true;
  let error = '';
  let editingPost = null;

  // Which list to render depends on the active tab
  $: displayPosts = activeTab === 'pending' ? pendingPosts : allPosts;

  onMount(async () => {
    if ($authStore.user?.role !== 'Admin') {
      error = "Access Denied: Administrator privileges required.";
      loading = false;
      return;
    }
    await loadAll();
  });

  // ── Data Loading ───────────────────────────────────────────────────────────

  async function loadAll() {
    loading = true;
    error = '';
    try {
      // Fetch both lists in parallel so switching tabs is instant
      const [pending, all] = await Promise.all([
        adminApi.pending(),
        adminApi.allPosts()
      ]);
      pendingPosts = pending || [];
      allPosts = all || [];
    } catch (e) {
      error = "Failed to load posts: " + e.message;
    } finally {
      loading = false;
    }
  }

  // ── Actions ────────────────────────────────────────────────────────────────

  async function handleApprove(id) {
    try {
      const safeId = String(id);
      await postsApi.update(safeId, { status: 'Approved' });
      // Remove from pending; update status in all-posts list without re-fetching
      pendingPosts = pendingPosts.filter(p => String(p.id) !== safeId);
      allPosts = allPosts.map(p => String(p.id) === safeId ? { ...p, status: 'Approved' } : p);
    } catch (e) {
      alert("Failed to approve: " + e.message);
    }
  }

  async function handleDelete(id) {
    if (!confirm("Are you sure you want to permanently delete this post?")) return;
    try {
      const safeId = String(id);
      await postsApi.remove(safeId);
      pendingPosts = pendingPosts.filter(p => String(p.id) !== safeId);
      allPosts = allPosts.filter(p => String(p.id) !== safeId);
    } catch (e) {
      alert("Delete failed: " + e.message);
    }
  }

  function startEdit(post) {
    editingPost = { ...post };
  }

  async function saveEdit() {
    try {
      const safeId = String(editingPost.id);
      await postsApi.update(safeId, {
        title:   editingPost.title,
        content: editingPost.content,
        status:  editingPost.status
      });
      // Update both lists in-place, then remove from pending if no longer pending
      const applyUpdate = arr => arr.map(p => String(p.id) === safeId ? { ...p, ...editingPost } : p);
      allPosts = applyUpdate(allPosts);
      pendingPosts = applyUpdate(pendingPosts).filter(p => (p.status || '').toLowerCase() === 'pending');
      editingPost = null;
    } catch (e) {
      alert("Update failed: " + e.message);
    }
  }

  // ── Helpers ────────────────────────────────────────────────────────────────

  function statusClass(status) {
    const s = (status || '').toLowerCase();
    if (s === 'approved') return 'badge-approved';
    if (s === 'rejected') return 'badge-rejected';
    return 'badge-pending';
  }

  function statusLabel(status) {
    const s = (status || '').toLowerCase();
    if (s === 'approved') return 'Approved';
    if (s === 'rejected') return 'Rejected';
    return 'Pending Review';
  }
</script>

<div class="h-32"></div>

<main class="max-w-6xl mx-auto px-6 pb-20">

  <!-- Header -->
  <div class="flex items-center justify-between mb-8">
    <div>
      <h1 class="text-4xl font-black text-white uppercase tracking-tighter">Admin Panel</h1>
      <p class="text-gray-400">Manage all community submissions.</p>
    </div>
    <button on:click={loadAll} class="p-3 bg-white/5 hover:bg-white/10 rounded-2xl text-white transition-all border border-white/10">
      ↺ Refresh
    </button>
  </div>

  <!-- Tabs -->
  <div class="flex gap-2 mb-6">
    <button
      class="tab-btn {activeTab === 'pending' ? 'tab-active' : ''}"
      on:click={() => activeTab = 'pending'}
    >
      Pending Review
      {#if pendingPosts.length > 0}
        <span class="ml-2 bg-yellow-500 text-black text-[10px] font-black px-2 py-0.5 rounded-full">
          {pendingPosts.length}
        </span>
      {/if}
    </button>

    <button
      class="tab-btn {activeTab === 'all' ? 'tab-active' : ''}"
      on:click={() => activeTab = 'all'}
    >
      All Posts
      <span class="ml-2 bg-white/10 text-white/50 text-[10px] font-black px-2 py-0.5 rounded-full">
        {allPosts.length}
      </span>
    </button>
  </div>

  <!-- List -->
  {#if loading}
    <div class="py-20 text-center text-blue-400 animate-pulse">Loading...</div>

  {:else if error}
    <div class="p-8 bg-red-500/10 border border-red-500/20 rounded-2xl text-red-400 text-center">{error}</div>

  {:else if displayPosts.length === 0}
    <div class="py-20 text-center bg-white/5 rounded-3xl border border-dashed border-white/10 text-white/30 italic">
      {activeTab === 'pending' ? 'No posts awaiting approval. ✓' : 'No posts found.'}
    </div>

  {:else}
    <div class="grid gap-4">
      {#each displayPosts as post (post.id)}
        <div class="bg-[#0f1219]/80 backdrop-blur-md border border-white/10 p-6 rounded-3xl flex flex-col md:flex-row justify-between gap-6">

          <div class="flex-grow min-w-0">
            <div class="flex flex-wrap items-center gap-3 mb-2">
              <span class="badge {statusClass(post.status)}">{statusLabel(post.status)}</span>
              <span class="text-white/30 text-xs">By {post.author_name}</span>
              <span class="text-white/20 text-[10px] ml-auto shrink-0">{post.category}</span>
            </div>
            <h3 class="text-xl font-bold text-white mb-2 truncate">{post.title}</h3>
            <p class="text-gray-400 line-clamp-2 text-sm">{post.description || ''}</p>
          </div>

          <div class="flex items-center gap-2 self-start shrink-0">
            {#if (post.status || '').toLowerCase() !== 'approved'}
              <button on:click={() => handleApprove(post.id)} class="btn-approve">Approve</button>
            {/if}
            <button on:click={() => startEdit(post)} class="btn-edit">Edit</button>
            <button on:click={() => handleDelete(post.id)} class="btn-delete">Delete</button>
          </div>

        </div>
      {/each}
    </div>
  {/if}

</main>

<!-- Edit Modal -->
{#if editingPost}
  <div class="fixed inset-0 z-[200] bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-[#161a23] border border-white/10 w-full max-w-2xl rounded-[2.5rem] p-10 shadow-2xl">
      <h2 class="text-2xl font-black text-white mb-6 uppercase">Edit Post</h2>
      <div class="space-y-4">
        <input bind:value={editingPost.title} class="modal-input" placeholder="Title" />
        <textarea bind:value={editingPost.content} rows="6" class="modal-input" placeholder="Content"></textarea>
        <div class="space-y-1">
          <label class="text-[10px] font-black text-white/40 uppercase tracking-widest">Status</label>
          <select bind:value={editingPost.status} class="modal-input">
            <option value="pending">Pending</option>
            <option value="Approved">Approved</option>
          </select>
        </div>
      </div>
      <div class="flex justify-end gap-4 mt-8">
        <button on:click={() => editingPost = null} class="text-white/40 font-bold hover:text-white transition-colors">Cancel</button>
        <button on:click={saveEdit} class="bg-blue-600 px-8 py-3 rounded-full text-white font-bold hover:bg-blue-500 transition-colors">Save Changes</button>
      </div>
    </div>
  </div>
{/if}

<style>
  @reference "../../app.css";

  .tab-btn {
    @apply flex items-center px-6 py-2.5 rounded-2xl text-sm font-bold text-white/50
           hover:text-white hover:bg-white/5 transition-all border border-transparent;
  }
  .tab-active { @apply bg-white/10 text-white border-white/10; }

  .badge          { @apply px-2 py-0.5 text-[10px] font-bold uppercase rounded tracking-tight; }
  .badge-pending  { @apply bg-yellow-500/20 text-yellow-400; }
  .badge-approved { @apply bg-green-500/20  text-green-400;  }
  .badge-rejected { @apply bg-red-500/20    text-red-400;    }

  .btn-approve { @apply px-5 py-2.5 bg-green-500 text-white rounded-xl text-xs font-black uppercase hover:bg-green-400 transition-all; }
  .btn-edit    { @apply px-5 py-2.5 bg-white/10 text-white rounded-xl text-xs font-black uppercase hover:bg-white/20 transition-all; }
  .btn-delete  { @apply px-5 py-2.5 bg-red-500/20 text-red-500 rounded-xl text-xs font-black uppercase hover:bg-red-500 hover:text-white transition-all; }
  .modal-input { @apply w-full bg-white/5 border border-white/10 rounded-2xl p-4 text-white outline-none focus:border-blue-500; }
</style>
<script>
  import { onMount } from 'svelte';
  import { admin as adminApi, posts as postsApi } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';

  let pendingPosts = [];
  let loading = true;
  let error = '';
  let editingPost = null;

  onMount(async () => {
    // SECURITY: Ensure UI doesn't render for non-admins
    if ($authStore.user?.role !== 'Admin') {
      error = "Access Denied: Administrator privileges required.";
      loading = false;
      return;
    }
    await loadPending();
  });

  async function loadPending() {
    loading = true;
    try {
      const data = await adminApi.pending();
      // Ensure we handle empty arrays or null responses
      pendingPosts = data || [];
    } catch (e) {
      error = "Failed to load queue: " + e.message;
    } finally {
      loading = false;
    }
  }

  async function handleApprove(id) {
    try {
      // DYNAMIC API: Updates status to 'Approved' (Matches main feed filter)
      await postsApi.update(id, { status: 'Approved' });
      
      // OPTIMISTIC UI: Remove from list locally for instant feedback
      pendingPosts = pendingPosts.filter(p => p.id !== id);
    } catch (e) {
      alert("Failed to approve: " + e.message);
    }
  }

  async function handleDelete(id) {
    if (!confirm("Are you sure you want to delete this post?")) return;
    try {
      await postsApi.remove(id);
      pendingPosts = pendingPosts.filter(p => p.id !== id);
    } catch (e) {
      alert("Delete failed: " + e.message);
    }
  }

  function startEdit(post) {
    editingPost = { ...post };
  }

  async function saveEdit() {
    try {
      await postsApi.update(editingPost.id, editingPost);
      editingPost = null;
      await loadPending(); // Reload to reflect any status/content changes
    } catch (e) {
      alert("Update failed: " + e.message);
    }
  }
</script>

<div class="h-32"></div>

<main class="max-w-6xl mx-auto px-6 pb-20">
  <div class="flex items-center justify-between mb-8">
    <div>
      <h1 class="text-4xl font-black text-white uppercase tracking-tighter">Moderation Queue</h1>
      <p class="text-gray-400">Review community submissions before they go live.</p>
    </div>
    <button on:click={loadPending} class="p-3 bg-white/5 hover:bg-white/10 rounded-2xl text-white transition-all border border-white/10">
      Refresh List
    </button>
  </div>

  {#if loading}
    <div class="py-20 text-center text-blue-400 animate-pulse">Loading queue...</div>
  {:else if error}
    <div class="p-8 bg-red-500/10 border border-red-500/20 rounded-2xl text-red-400 text-center">{error}</div>
  {:else if pendingPosts.length === 0}
    <div class="py-20 text-center bg-white/5 rounded-3xl border border-dashed border-white/10 text-white/30 italic">
      No posts currently awaiting approval.
    </div>
  {:else}
    <div class="grid gap-4">
      {#each pendingPosts as post}
        <div class="bg-[#0f1219]/80 backdrop-blur-md border border-white/10 p-6 rounded-3xl flex flex-col md:flex-row justify-between gap-6">
          <div class="flex-grow">
            <div class="flex items-center gap-3 mb-2">
              <span class="px-2 py-0.5 bg-yellow-500/20 text-yellow-500 text-[10px] font-bold uppercase rounded">Pending Review</span>
              <span class="text-white/30 text-xs">By {post.author_name}</span>
            </div>
            <h3 class="text-xl font-bold text-white mb-2">{post.title}</h3>
            <p class="text-gray-400 line-clamp-2 text-sm">{post.content}</p>
          </div>

          <div class="flex items-center gap-2 self-start">
            <button on:click={() => handleApprove(post.id)} class="btn-approve">Approve</button>
            <button on:click={() => startEdit(post)} class="btn-edit">Edit</button>
            <button on:click={() => handleDelete(post.id)} class="btn-delete">Delete</button>
          </div>
        </div>
      {/each}
    </div>
  {/if}
</main>

{#if editingPost}
  <div class="fixed inset-0 z-[200] bg-black/90 backdrop-blur-md flex items-center justify-center p-4">
    <div class="bg-[#161a23] border border-white/10 w-full max-w-2xl rounded-[2.5rem] p-10 shadow-2xl">
      <h2 class="text-2xl font-black text-white mb-6 uppercase">Admin Edit</h2>
      <div class="space-y-4">
        <input bind:value={editingPost.title} class="modal-input" placeholder="Title" />
        <textarea bind:value={editingPost.content} rows="6" class="modal-input" placeholder="Content"></textarea>
      </div>
      <div class="flex justify-end gap-4 mt-8">
        <button on:click={() => editingPost = null} class="text-white/40 font-bold">Cancel</button>
        <button on:click={saveEdit} class="bg-blue-600 px-8 py-3 rounded-full text-white font-bold">Save Changes</button>
      </div>
    </div>
  </div>
{/if}

<style>
  @reference "../../app.css";
  .btn-approve { @apply px-5 py-2.5 bg-green-500 text-white rounded-xl text-xs font-black uppercase hover:bg-green-400 transition-all; }
  .btn-edit { @apply px-5 py-2.5 bg-white/10 text-white rounded-xl text-xs font-black uppercase hover:bg-white/20 transition-all; }
  .btn-delete { @apply px-5 py-2.5 bg-red-500/20 text-red-500 rounded-xl text-xs font-black uppercase hover:bg-red-500 hover:text-white transition-all; }
  .modal-input { @apply w-full bg-white/5 border border-white/10 rounded-2xl p-4 text-white outline-none focus:border-blue-500; }
</style>
<script>
  import { admin } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';

  let pendingPosts = $state([]);
  let loading      = $state(true);
  let fetchError   = $state('');

  $effect(() => {
    if (!authStore.isLoggedIn) { loading = false; return; }
    admin.pending()
      .then(data => { pendingPosts = data; })
      .catch(err  => { fetchError  = err.data?.msg ?? err.message; })
      .finally(()  => { loading    = false; });
  });
</script>

<div class="h-32"></div>
<section class="max-w-7xl mx-auto px-6 mb-20">
  <div class="flex justify-between items-end mb-10">
    <div>
      <p class="text-[10px] font-black text-red-400 tracking-widest uppercase mb-2">Internal Dashboard</p>
      <h1 class="text-4xl font-bold text-white">Management Panel</h1>
    </div>
    <div class="flex gap-4">
      <div class="bg-[#1A1F2E] px-6 py-2 rounded-xl border border-white/5 text-center">
        <p class="text-[10px] text-gray-500 uppercase font-bold">Pending Reviews</p>
        <p class="text-xl font-bold text-yellow-400">{loading ? '…' : pendingPosts.length}</p>
      </div>
    </div>
  </div>

  {#if !authStore.isLoggedIn || authStore.user?.role !== 'Admin'}
    <div class="py-20 text-center text-gray-400">Admin access required.</div>
  {:else if loading}
    <div class="py-20 flex justify-center">
      <div class="size-10 border-2 border-red-500 border-t-transparent rounded-full animate-spin"></div>
    </div>
  {:else}
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
    <div class="lg:col-span-2 bg-[#1A1F2E] rounded-[2.5rem] border border-white/5 p-8">
      <h2 class="text-lg font-bold text-white mb-6">Review Queue</h2>
      {#if fetchError}
        <p class="text-red-400">{fetchError}</p>
      {:else if pendingPosts.length === 0}
        <p class="text-gray-500 italic">No posts pending review.</p>
      {:else}
        <div class="space-y-3">
          {#each pendingPosts as post}
            <div class="bg-black/20 p-4 rounded-2xl border border-white/5 flex items-center justify-between">
              <div>
                <p class="text-sm font-bold text-white">{post.title}</p>
                <p class="text-[10px] text-gray-500 uppercase">By {post.author} • {post.category}</p>
              </div>
              <div class="flex gap-2">
                <button class="bg-green-500/20 text-green-400 px-4 py-1.5 rounded-lg text-xs font-bold hover:bg-green-500/30">Approve</button>
                <button class="bg-red-500/20 text-red-400 px-4 py-1.5 rounded-lg text-xs font-bold hover:bg-red-500/30">Reject</button>
              </div>
            </div>
          {/each}
        </div>
      {/if}
    </div>

    <div class="bg-[#1A1F2E] rounded-[2.5rem] border border-white/5 p-8 flex flex-col gap-4">
      <h2 class="text-lg font-bold text-white mb-2">Quick Actions</h2>
      <button class="w-full py-4 bg-white/5 rounded-2xl border border-white/5 text-sm font-bold hover:bg-white/10 text-left px-6">Manage Users</button>
      <button class="w-full py-4 bg-white/5 rounded-2xl border border-white/5 text-sm font-bold hover:bg-white/10 text-left px-6">Platform Analytics</button>
      <button class="w-full py-4 bg-white/5 rounded-2xl border border-white/5 text-sm font-bold hover:bg-white/10 text-left px-6">System Logs</button>
    </div>
  </div>
  {/if}
</section>

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
        <p class="text-xl font-bold text-yellow-400">12</p>
      </div>
    </div>
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
    <div class="lg:col-span-2 bg-[#1A1F2E] rounded-[2.5rem] border border-white/5 p-8">
      <h2 class="text-lg font-bold text-white mb-6">Review Queue</h2>
      <div class="space-y-3">
        {#each [1, 2, 3] as i}
          <div class="bg-black/20 p-4 rounded-2xl border border-white/5 flex items-center justify-between">
            <div class="flex gap-4 items-center">
              <div class="size-10 bg-white/5 rounded-lg flex items-center justify-center text-xl">Review</div>
              <div>
                <p class="text-sm font-bold text-white">The Future of AI in Design</p>
                <p class="text-[10px] text-gray-500 uppercase">By Alex R. • 5 min read</p>
              </div>
            </div>
            <div class="flex gap-2">
              <button class="bg-green-500/20 text-green-400 px-4 py-1.5 rounded-lg text-xs font-bold hover:bg-green-500/30">Approve</button>
              <button class="bg-red-500/20 text-red-400 px-4 py-1.5 rounded-lg text-xs font-bold hover:bg-red-500/30">Reject</button>
            </div>
          </div>
        {/each}
      </div>
    </div>

    <div class="bg-[#1A1F2E] rounded-[2.5rem] border border-white/5 p-8 flex flex-col gap-4">
      <h2 class="text-lg font-bold text-white mb-2">Quick Actions</h2>
      <button class="w-full py-4 bg-white/5 rounded-2xl border border-white/5 text-sm font-bold hover:bg-white/10 text-left px-6">Manage Users</button>
      <button class="w-full py-4 bg-white/5 rounded-2xl border border-white/5 text-sm font-bold hover:bg-white/10 text-left px-6">Platform Analytics</button>
      <button class="w-full py-4 bg-white/5 rounded-2xl border border-white/5 text-sm font-bold hover:bg-white/10 text-left px-6">System Logs</button>
    </div>
  </div>
</section>
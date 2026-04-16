<script>
  // Ensure onRead is a prop so the button knows where to go
  let { title, description, image, tags, onRead } = $props();
</script>

<div class="group relative aspect-[4/3] w-full overflow-hidden rounded-[2.5rem] border border-white/10 bg-[#1A1F2E] shadow-xl transition-all duration-500 hover:shadow-2xl hover:shadow-blue-500/20">
  
  <img 
    src={image} 
    alt={title} 
    class="absolute inset-0 h-full w-full object-cover transition-transform duration-700 group-hover:scale-110 group-hover:brightness-[0.3]" 
  />

  <div class="absolute inset-0 flex flex-col justify-end p-8 bg-gradient-to-t from-black/90 via-black/20 to-transparent transition-opacity duration-300 group-hover:opacity-0">
    <h3 class="text-xl font-bold text-white leading-tight">{title}</h3>
  </div>

  <div class="absolute inset-0 flex flex-col justify-between p-7 opacity-0 translate-y-2 transition-all duration-500 group-hover:opacity-100 group-hover:translate-y-0">
    
    <div class="space-y-3">
      <h3 class="text-xl font-bold text-white leading-tight">{title}</h3>
      <p class="text-sm text-gray-300 line-clamp-4 leading-relaxed">
        {description}
      </p>
      <div class="flex flex-wrap gap-2">
        {#each tags as tag}
          <span class="text-[10px] text-gray-500 font-medium uppercase tracking-wider">#{tag.replace('#', '')}</span>
        {/each}
      </div>
    </div>

    <div class="flex items-center justify-between pb-1">
      <div class="flex gap-4 items-center">
        <button class="text-white/40 hover:text-white transition-colors cursor-pointer">
          <svg class="size-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" /></svg>
        </button>
        <button class="text-white/40 hover:text-white transition-colors cursor-pointer">
          <svg class="size-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" /></svg>
        </button>
        <button class="text-white/40 hover:text-red-400 transition-colors cursor-pointer">
          <svg class="size-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" /></svg>
        </button>
      </div>

      <button 
        onclick={(e) => { e.stopPropagation(); onRead(); }}
        class="bg-white text-black px-7 py-2.5 rounded-2xl text-sm font-bold hover:bg-gray-200 transition-all active:scale-95 cursor-pointer shadow-lg"
      >
        Read
      </button>
    </div>
  </div>
</div>
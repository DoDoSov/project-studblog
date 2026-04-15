<section class="mx-4 my-16 relative overflow-hidden">
  <div class="bg-brand-card/30 backdrop-blur-md rounded-[2.5rem] p-12 border border-white/5 flex flex-col items-center text-center relative">
    
    <div class="absolute top-6 left-6 opacity-20 pointer-events-none">
      <div class="grid grid-cols-4 gap-2">
        {#each Array(12) as _}
          <div class="size-1 bg-white rounded-full"></div>
        {/each}
      </div>
    </div>

    <h2 class="text-3xl md:text-4xl font-bold text-white mb-4 tracking-tight">
      Ready to Share What You Know?
    </h2>
    
    <p class="text-gray-400 text-lg mb-8 max-w-xl">
      Join <span class="text-white font-bold">1,240</span> student writers. 
      Publish your first article in minutes — free forever.
    </p>

    <div class="w-full max-w-md">
      <div class="flex flex-col sm:flex-row gap-3">
        <input 
          type="email" 
          placeholder="your@university.edu" 
          class="flex-grow bg-black/20 border border-white/10 rounded-2xl px-6 py-4 text-white outline-none focus:ring-2 ring-blue-500/50 transition-all placeholder:text-gray-600"
        />
        <button class="bg-[#5D5CFF] hover:bg-[#4A49E5] text-white font-bold px-8 py-4 rounded-2xl transition-all shadow-lg shadow-blue-500/20 active:scale-95 whitespace-nowrap">
          Join —>
        </button>
      </div>
      
      <p class="mt-4 text-xs text-gray-500 font-medium tracking-wide uppercase">
        No credit card. No paywall.
      </p>
    </div>

    <div class="absolute bottom-6 right-6 opacity-20 pointer-events-none rotate-180">
      <div class="grid grid-cols-4 gap-2">
        {#each Array(12) as _}
          <div class="size-1 bg-white rounded-full"></div>
        {/each}
      </div>
    </div>
  </div>
</section>
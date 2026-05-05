<script>
  /**
   * Svelte 4 Prop Migration
   * We use 'export let' to define properties.
   * To achieve the $bindable behavior, the parent must use 'bind:openModal={variable}'.
   */
  export let openModal = null;
</script>

<footer class="bg-[#1A1F2E] border-t border-white/5 rounded-t-[3rem] mt-20 p-12 text-gray-400">
  <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
    
    <!-- Brand Section -->
    <div>
      <h3 class="text-white font-bold text-xl mb-4 tracking-tight">StudPlace 2026</h3>
      <p class="text-sm leading-relaxed opacity-60">
        The premier open-source platform for student research, lifestyle, and academic insights.
      </p>
    </div>
    
    <!-- Legal Navigation -->
    <div class="flex flex-col items-center md:items-start gap-3">
      <span class="text-white font-bold text-xl mb-4 tracking-tight">Legal</span>
      <button 
        on:click={() => openModal = 'privacy'} 
        class="hover:text-blue-400 text-sm transition-colors cursor-pointer text-left w-fit"
      >
        Privacy Policy
      </button>
      <button 
        on:click={() => openModal = 'terms'} 
        class="hover:text-blue-400 text-sm transition-colors cursor-pointer text-left w-fit"
      >
        Terms of Service
      </button>
    </div>

    <!-- Copyright Section -->
    <div class="flex flex-col md:text-right md:justify-end">
      <p class="text-sm">&copy; 2026 StudPlace.</p>
      <p class="text-[10px] mt-2 italic font-black text-blue-500 uppercase tracking-widest">
        Built with Love
      </p>
    </div>
  </div>
</footer>
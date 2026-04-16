<script>
  let { openModal = $bindable() } = $props(); // Pass this up to App.svelte to show the modal
</script>

<footer class="bg-[#1A1F2E] border-t border-white/5 rounded-t-[3rem] mt-20 p-12 text-gray-400">
  <div class="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
    <div>
      <h3 class="text-white font-serif text-xl font-bold mb-4">StudPlace 2026</h3>
      <p class="text-sm leading-relaxed">The premier open-source platform for student research, lifestyle, and academic insights.</p>
    </div>
    
    <div class="flex flex-col gap-3">
      <span class="text-white font-serif text-xl font-bold mb-4">Legal</span>
      <button 
        onclick={() => openModal = 'privacy'} 
        class="hover:text-white text-sm transition-colors cursor-pointer text-center"
      >
        Privacy Policy
      </button>
      <button 
        onclick={() => openModal = 'terms'} 
        class="hover:text-white text-sm transition-colors cursor-pointer text-center"
      >
        Terms of Service
      </button>
    </div>

    <div class="flex flex-col md:text-right justify-end">
      <p class="text-sm">&copy; 2026 StudPlace.</p>
      <p class="text-[10px] mt-2 italic font-medium uppercase tracking-tighter">Built with Love</p>
    </div>
  </div>
</footer>
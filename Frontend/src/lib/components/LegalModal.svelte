<script>
  /**
   * Svelte 4 Prop Migration
   * 'export let' allows the parent to pass this value.
   * To achieve the $bindable behavior, the parent must use 'bind:type={variable}'.
   */
  export let type = null;

  const content = {
    privacy: {
      title: "Privacy Policy",
      text: "We value your privacy. StudPlace only collects university email addresses for verification purposes. We do not sell your data to third parties. Cookies are used only to keep you logged in."
    },
    terms: {
      title: "Terms of Service",
      text: "By using StudPlace, you agree to post content that is respectful and academic in nature. Plagiarism is grounds for account suspension. You retain ownership of your words, but grant us a license to display them."
    }
  };

  function close() {
    type = null;
  }
</script>

{#if type}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div 
    class="fixed inset-0 bg-black/80 backdrop-blur-sm z-[100] flex items-center justify-center p-6"
    on:click={close}
  >
    <!-- stopPropagation ensures clicking the modal body doesn't trigger the outer 'close' -->
    <div 
      class="bg-[#1A1F2E] border border-white/10 w-full max-w-2xl rounded-[2.5rem] p-10 shadow-2xl relative"
      on:click|stopPropagation
    >
      <button 
        on:click={close}
        class="absolute top-6 right-8 text-gray-500 hover:text-white text-2xl transition-colors"
      >
        &times;
      </button>

      <p class="text-[10px] font-black text-purple-400 tracking-widest uppercase mb-2">Legal Document</p>
      <h2 class="text-3xl font-bold text-white mb-6">{content[type].title}</h2>
      
      <div class="max-h-[60vh] overflow-y-auto pr-4 custom-scrollbar">
        <p class="text-gray-400 leading-relaxed whitespace-pre-wrap">
          {content[type].text}
        </p>
      </div>

      <button 
        on:click={close}
        class="mt-8 w-full py-4 bg-white/5 hover:bg-white/10 border border-white/5 rounded-2xl text-white font-bold transition-all active:scale-95"
      >
        I Understand
      </button>
    </div>
  </div>
{/if}

<style>
  /* Svelte 4 Custom Scrollbar Styling */
  .custom-scrollbar::-webkit-scrollbar {
    width: 4px;
  }
  .custom-scrollbar::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
  }

  /* Note: Svelte 5 'animate-in' classes replaced with standard CSS or 
     Tailwind transitions for compatibility if your plugin isn't active. */
</style>
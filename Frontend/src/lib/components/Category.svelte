<script>
  import LeftArrow from '../../assets/Category/left-arrow.svg';
  import RightArrow from '../../assets/Category/right-arrow.svg';

  let categories = ["Technology", "Finance", "Business", "Health", "Travel", "Science", "Education", "Lifestyle", "Engineering", "Sports", "AI"];
  let active = "Technology";
</script>

<div class="mx-4 mb-6">
  <div class="bg-brand-card/40 backdrop-blur-sm p-2 rounded-2xl border bg-[#2D364F]/30 border-white/5 flex items-center gap-2">
    
    <button class="p-2 hover:bg-white/5 rounded-xl transition-colors group">
      <img src={LeftArrow} class="size-4 opacity-50 group-hover:opacity-100 brightness-200" alt="Prev" />
    </button>

    <div class="flex-grow overflow-hidden">
      <ul class="flex items-center gap-1 overflow-x-auto no-scrollbar whitespace-nowrap py-1">
        {#each categories as cat}
          <li>
            <button 
              onclick={() => active = cat}
              class="px-5 py-2 rounded-xl text-sm font-medium transition-all duration-200
              {active === cat 
                ? 'bg-brand-light text-white shadow-lg' 
                : 'text-gray-400 hover:text-gray-200 hover:bg-white/5'}"
            >
              {cat}
            </button>
          </li>
        {/each}
      </ul>
    </div>

    <button class="p-2 hover:bg-white/5 rounded-xl transition-colors group">
      <img src={RightArrow} class="size-4 opacity-50 group-hover:opacity-100 brightness-200" alt="Next" />
    </button>

  </div>
</div>

<style>
  .no-scrollbar::-webkit-scrollbar { display: none; }
  .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>
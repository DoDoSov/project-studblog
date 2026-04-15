<script>
  let { category, title, description, author, initials, likes, icon } = $props();

  // Mapping categories to match the colorful text in your mockup
  const colors = {
    HEALTH: "text-[#4ADE80]",
    FINANCE: "text-[#FACC15]",
    SCIENCE: "text-[#2DD4BF]"
  };
</script>

<div class="bg-brand-card/40 rounded-[2rem] p-5 border border-white/5 flex flex-col h-full hover:bg-brand-card/60 transition-all duration-300 group">
  
  <div class="bg-black/20 rounded-2xl h-36 mb-5 flex items-center justify-center border border-white/5 relative overflow-hidden">
     <div class="absolute inset-0 opacity-10 pointer-events-none" style="background-image: radial-gradient(circle, white 1px, transparent 1px); background-size: 12px 12px;"></div>
     
     <img src={icon} class="size-12 group-hover:scale-110 transition-transform duration-500" alt="" />
  </div>

  <span class="text-[11px] font-black tracking-widest bg-white/5 px-2 py-1 rounded-md w-fit mb-3 {colors[category]}">
    {category}
  </span>

  <h3 class="text-white font-bold text-lg leading-tight mb-2">
    {title}
  </h3>
  <p class="text-gray-400 text-sm line-clamp-2 mb-6 font-medium">
    {description}
  </p>

  <div class="mt-auto pt-4 border-t border-white/5 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <div class="size-9 rounded-full flex items-center justify-center text-xs font-bold text-white
        {category === 'HEALTH' ? 'bg-[#4ADE80]/80' : category === 'FINANCE' ? 'bg-[#FACC15]/80' : 'bg-[#2DD4BF]/80'}">
        {initials}
      </div>
      <span class="text-gray-400 text-sm font-semibold">{author}</span>
    </div>
    
    <div class="flex items-center gap-1.5 text-gray-500 text-xs font-mono">
      <span class="text-lg">♡</span>
      <span>{likes}</span>
    </div>
  </div>
</div>
<script>
  const writingRules = [
    { title: "Originality", text: "Plagiarism is strictly prohibited. All content must be your own work." },
    { title: "Clarity", text: "Use clear, concise language. Avoid heavy academic jargon where possible." },
    { title: "Formatting", text: "Use proper headings and code blocks to keep your article readable." }
  ];

  const commentRules = [
    { title: "Respect", text: "Critique the idea, not the person. Maintain a professional tone." },
    { title: "No Spam", text: "Self-promotion and repetitive links will be removed immediately." },
    { title: "Constructive", text: "Try to add value to the conversation with your feedback." }
  ];
</script>

<div class="h-32"></div>

<section class="max-w-6xl mx-auto px-6 mb-20">
  <!-- Header Section -->
  <header class="bg-white/5 p-10 rounded-[3rem] border border-white/10 mb-12">
    <p class="text-[10px] font-black text-blue-400 tracking-[0.3em] uppercase mb-4">Community Standards</p>
    <h1 class="text-5xl font-black text-white">Guidelines</h1>
    <p class="text-white/40 mt-4 max-w-2xl">To maintain a high-quality learning environment, all students are expected to follow these core principles when contributing.</p>
  </header>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <!-- Writing Rules Column -->
    <div class="glass-panel p-8 rounded-[2.5rem]">
      <div class="flex items-center gap-4 mb-8">
        <span class="bg-blue-500/20 p-4 rounded-2xl text-2xl shadow-inner shadow-blue-500/10">✍️</span>
        <h2 class="text-2xl font-bold text-white">Writing Rules</h2>
      </div>
      
      <div class="space-y-4">
        {#each writingRules as rule}
          <div class="bg-white/5 p-6 rounded-[1.5rem] border border-white/5 hover:border-blue-500/30 transition-colors duration-300">
            <h3 class="text-blue-400 font-bold text-xs mb-2 uppercase tracking-widest">{rule.title}</h3>
            <p class="text-white/60 text-sm leading-relaxed">{rule.text}</p>
          </div>
        {/each}
      </div>
    </div>

    <!-- Comment Rules Column -->
    <div class="glass-panel p-8 rounded-[2.5rem]">
      <div class="flex items-center gap-4 mb-8">
        <span class="bg-emerald-500/20 p-4 rounded-2xl text-2xl shadow-inner shadow-emerald-500/10">💬</span>
        <h2 class="text-2xl font-bold text-white">Comment Rules</h2>
      </div>
      
      <div class="space-y-4">
        {#each commentRules as rule}
          <div class="bg-white/5 p-6 rounded-[1.5rem] border border-white/5 hover:border-emerald-500/30 transition-colors duration-300">
            <h3 class="text-emerald-400 font-bold text-xs mb-2 uppercase tracking-widest">{rule.title}</h3>
            <p class="text-white/60 text-sm leading-relaxed">{rule.text}</p>
          </div>
        {/each}
      </div>
    </div>
  </div>
</section>

<style>
  /* Tailwind 4.0 custom glass utility defined in app.css */
  .glass-panel {
    background-color: rgba(15, 18, 25, 0.7);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
  }
</style>
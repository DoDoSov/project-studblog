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

<section class="max-w-6xl mx-auto px-6 mb-20 animate-in fade-in slide-in-from-bottom-6 duration-700">
  <div class="mb-12">
    <p class="text-[10px] font-black text-blue-400 tracking-widest uppercase mb-2">Community Standards</p>
    <h1 class="text-4xl font-bold text-white">Guidelines</h1>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <div class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl">
      <div class="flex items-center gap-4 mb-8">
        <span class="bg-blue-500/20 p-3 rounded-2xl text-2xl">✍️</span>
        <h2 class="text-2xl font-bold text-white">Writing Rules</h2>
      </div>
      <div class="space-y-4">
        {#each writingRules as rule}
          <div class="bg-white/5 p-5 rounded-2xl border border-white/5">
            <h3 class="text-blue-400 font-bold text-sm mb-1 uppercase tracking-wider">{rule.title}</h3>
            <p class="text-gray-400 text-sm leading-relaxed">{rule.text}</p>
          </div>
        {/each}
      </div>
    </div>

    <div class="bg-[#1A1F2E] p-8 rounded-[2.5rem] border border-white/5 shadow-2xl">
      <div class="flex items-center gap-4 mb-8">
        <span class="bg-green-500/20 p-3 rounded-2xl text-2xl">💬</span>
        <h2 class="text-2xl font-bold text-white">Comment Rules</h2>
      </div>
      <div class="space-y-4">
        {#each commentRules as rule}
          <div class="bg-white/5 p-5 rounded-2xl border border-white/5">
            <h3 class="text-green-400 font-bold text-sm mb-1 uppercase tracking-wider">{rule.title}</h3>
            <p class="text-gray-400 text-sm leading-relaxed">{rule.text}</p>
          </div>
        {/each}
      </div>
    </div>
  </div>
</section>
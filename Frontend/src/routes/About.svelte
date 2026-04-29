<script>
  const steps = [
    {
      id: "STEP 01",
      title: "Create an Account",
      desc: "Sign up with your university email or continue with Google OAuth. Verification takes under 60 seconds.",
      icon: "✍️"
    },
    {
      id: "STEP 02",
      title: "Write Your Post",
      desc: "Use the rich text editor to compose your article. Add images from Imgur or browse Unsplash for free stock photos.",
      icon: "📝"
    },
    {
      id: "STEP 03",
      title: "Editor Reviews",
      desc: "Our volunteer editors ensure quality and adherence to community guidelines. Approval usually happens within 24 hours.",
      icon: "✅"
    },
    {
      id: "STEP 04",
      title: "Go Live & Share",
      desc: "Your article is published on the platform. Share it via link, embed it elsewhere, or watch readers comment and engage.",
      icon: "🌍"
    }
  ];
</script>

<div class="h-32"></div>

<section class="bg-[#283047] py-4 rounded-2xl max-w-6xl mx-auto px-6 mb-20 animate-in fade-in slide-in-from-bottom-6 duration-700">
  <div class="bg-[#1A1F2E] p-10 md:p-16 rounded-[3rem] border border-white/5 shadow-2xl mb-12 relative overflow-hidden">
    <div class="relative z-10 max-w-2xl">
      <p class="text-[10px] font-black text-blue-400 tracking-[0.2em] uppercase mb-4">How it works</p>
      <h1 class="text-5xl md:text-6xl font-serif font-bold text-white leading-tight mb-6">
        Built for Students
      </h1>
      <p class="text-gray-400 text-lg leading-relaxed">
        StudBlogs is modeled after the best parts of Dev.to and Hackernoon — open, community-driven, and free. We provide a space for academic insights and student life.
      </p>
    </div>
    <div class="absolute -right-10 -bottom-10 opacity-5 text-[240px] pointer-events-none rotate-12">🎓</div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
    {#each steps as step}
      <div class="bg-[#1A1F2E] p-8 rounded-[2rem] border border-white/5 hover:border-white/20 transition-all group">
        <div class="text-4xl mb-6 group-hover:scale-110 transition-transform duration-300 inline-block">{step.icon}</div>
        <p class="text-[10px] font-black text-blue-400 tracking-widest uppercase mb-2">{step.id}</p>
        <h3 class="text-xl font-bold text-white mb-4">{step.title}</h3>
        <p class="text-gray-400 text-sm leading-relaxed">{step.desc}</p>
      </div>
    {/each}
  </div>

  <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-12">
    <div class="lg:col-span-2 bg-purple-600/10 border border-purple-500/20 p-10 rounded-[2.5rem] flex flex-col justify-center">
       <h2 class="text-3xl font-bold text-white mb-4">Our Core Mission</h2>
       <p class="text-purple-200/70 text-lg">To bridge the gap between academic theory and real-world application through student-led storytelling.</p>
    </div>
    <div class="bg-[#1A1F2E] border border-white/5 p-10 rounded-[2.5rem] flex items-center justify-center">
        <div class="text-center">
          <p class="text-4xl font-bold text-white">1,240+</p>
          <p class="text-xs text-gray-500 uppercase tracking-widest mt-2">Active Writers</p>
        </div>
    </div>
  </div>
</section>
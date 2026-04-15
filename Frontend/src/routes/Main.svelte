<script>
  import Category from '../lib/components/Category.svelte';
  import PostCard from '../lib/components/PostCard.svelte';
  import PostCardSmall from '../lib/components/PostCardSmall.svelte';
  import Promo from '../lib/components/Promo.svelte';

  const trendingPosts = [
    { title: "Getting Started with JavaScript in 2026", description: "A beginner-friendly guide...", image: "https://picsum.photos/seed/js/600/400", tags: ["JavaScript", "WebDev"] },
    { title: "Why React Still Dominates Frontend Development", description: "An overview...", image: "https://picsum.photos/seed/react/600/400", tags: ["React", "Frontend"] },
    { title: "Understanding REST APIs with Real Examples", description: "Learn how REST APIs work...", image: "https://picsum.photos/seed/api/600/400", tags: ["API", "Backend"] }
  ];

  const latestPosts = [
    { title: "The Future of AI in Web Design", description: "How generative tools...", image: "https://picsum.photos/seed/ai-web/600/400", tags: ["AI", "Design"] },
    { title: "Mastering Tailwind v4", description: "Everything you need...", image: "https://picsum.photos/seed/tailwind/600/400", tags: ["CSS", "Tailwind"] },
    { title: "10 Tips for Remote Developers", description: "Staying productive...", image: "https://picsum.photos/seed/remote/600/400", tags: ["Lifestyle", "Career"] }
  ];

  const morePosts = [
    { category: "HEALTH", title: "How I Fixed My Sleep During Exam Season", description: "Science-backed sleep protocol...", author: "Elena L.", initials: "EL", likes: 315 },
    { category: "FINANCE", title: "Student Investing 101: €200 → €1,400 in 18 Months", description: "Consistent ETF investing...", author: "Lukas P.", initials: "LP", likes: 203 },
    { category: "SCIENCE", title: "CRISPR in 2026: Student Labs Join Gene Editing", description: "How university students...", author: "Maria K.", initials: "MK", likes: 89 }
  ];
</script>

<div class="h-36"></div>
<div class="bg-[#1A1F2E] rounded-tr-[3rem] rounded-tl-[3rem] flex flex-col min-h-screen text-white font-sans shadow-[0_-20px_50px_rgba(0,0,0,0.5)]">
  <div class="h-6"></div>
  <Category />

  <section class="m-4 bg-[#2D364F]/30 p-6 rounded-3xl border border-white/5">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-bold text-white px-4 py-1 bg-white/5 rounded-lg">Trending</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {#each trendingPosts as post}
        <PostCard {...post} />
      {/each}
    </div>
  </section>

  <section class="mx-4 mb-10 bg-brand-card/10 p-6 rounded-3xl border border-white/5">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-bold text-white px-4 py-1 bg-white/5 rounded-lg">Latest</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {#each latestPosts as post}
        <PostCard {...post} />
      {/each}
    </div>
  </section>

  <section class="mx-4 mb-10 bg-brand-card/10 p-6 rounded-3xl border border-white/5">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-bold text-white px-4 py-1 bg-white/5 rounded-lg">More Posts</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {#each morePosts as post}
        <PostCardSmall {...post} />
      {/each}
    </div>
  </section>

  <Promo />
</div>
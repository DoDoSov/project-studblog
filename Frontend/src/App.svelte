<script>
  import GlassyStars from './lib/components/GlassyStars.svelte';
  import Branding from './lib/components/Branding.svelte';
  import Navbar from './lib/components/Navbar.svelte';
  import Footer from './lib/components/Footer.svelte';
  import Category from './lib/components/Category.svelte';
  import PostCard from './lib/components/PostCard.svelte';
  import PostCardSmall from './lib/components/PostCardSmall.svelte';
  import Promo from './lib/components/Promo.svelte';

  const trendingPosts = [
    {
      title: "Getting Started with JavaScript in 2026",
      description: "A beginner-friendly guide to understanding the basics of JavaScript and building your first interactive page.",
      image: "https://picsum.photos/seed/js/600/400",
      tags: ["JavaScript", "WebDev", "Beginner"]
    },
    {
      title: "Why React Still Dominates Frontend Development",
      description: "An overview of why React remains the most popular choice for modern web apps.",
      image: "https://picsum.photos/seed/react/600/400",
      tags: ["React", "Frontend", "Career"]
    },
    {
      title: "Understanding REST APIs with Real Examples",
      description: "Learn how REST APIs work and how to use them in your projects with clear, real-world scenarios.",
      image: "https://picsum.photos/seed/api/600/400",
      tags: ["API", "Backend", "Logic"]
    }
  ];
  const latestPosts = [
    {
      title: "The Future of AI in Web Design",
      description: "How generative tools are changing the way we think about user interfaces.",
      image: "https://picsum.photos/seed/ai-web/600/400",
      tags: ["AI", "Design", "2026"]
    },
    {
      title: "Mastering Tailwind v4",
      description: "Everything you need to know about the new CSS-first engine.",
      image: "https://picsum.photos/seed/tailwind/600/400",
      tags: ["CSS", "Tailwind", "Frontend"]
    },
    {
      title: "10 Tips for Remote Developers",
      description: "Staying productive and healthy while working from anywhere in the world.",
      image: "https://picsum.photos/seed/remote/600/400",
      tags: ["Lifestyle", "Career"]
    }
  ];
  const morePosts = [
    {
      category: "HEALTH",
      title: "How I Fixed My Sleep During Exam Season",
      description: "Science-backed sleep protocol for stressful university weeks — no caffeine required.",
      author: "Elena L.",
      initials: "EL",
      likes: 315
    },
    {
      category: "FINANCE",
      title: "Student Investing 101: €200 → €1,400 in 18 Months",
      description: "Consistent ETF investing and compounding knowledge — my entire journey.",
      author: "Lukas P.",
      initials: "LP",
      likes: 203
    },
    {
      category: "SCIENCE",
      title: "CRISPR in 2026: Student Labs Join Gene Editing",
      description: "How university students are contributing to real CRISPR breakthroughs.",
      author: "Maria K.",
      initials: "MK",
      likes: 89
    }
  ];
</script>


<Branding />
<GlassyStars />
<Navbar />

<div class="h-36"></div>
<div class="bg-[#1A1F2E] rounded-tr-xl rounded-tl-xl flex flex-col min-h-screen bg-brand-dark text-white font-sans">
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

  <Footer />
</div>

<style lang="postcss">
  @reference "tailwindcss";
  :global(html) {
    
  }
</style>
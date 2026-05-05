<script>
  import { auth } from '../../lib/api.js';
  import { authStore } from '../../lib/store.js';

  let { onSuccess } = $props(); // called with user after login/register

  let isLogin   = $state(true);
  let firstName = $state('');
  let email     = $state('');
  let password  = $state('');
  let error     = $state('');
  let loading   = $state(false);

  import bg from '../../assets/Login/login-bg.jpg';

  function toggleMode() {
    isLogin = !isLogin;
    error   = '';
  }

  async function handleSubmit() {
    error   = '';
    loading = true;
    try {
      if (isLogin) {
        const data = await auth.login({ email, password });
        authStore.setSession(data.access_token, data.user);
        onSuccess?.(data.user);
      } else {
        await auth.register({ first_name: firstName, email, password });
        // Auto-login after register
        const data = await auth.login({ email, password });
        authStore.setSession(data.access_token, data.user);
        onSuccess?.(data.user);
      }
    } catch (err) {
      error = err.data?.msg ?? err.message ?? 'Something went wrong';
    } finally {
      loading = false;
    }
  }
</script>

<div class="h-32"></div>

<section class="max-w-4xl mx-auto px-6 mb-20">
  <div class="bg-[#1A1F2E] rounded-[3rem] border border-white/5 overflow-hidden shadow-2xl flex flex-col md:flex-row min-h-[550px] transition-all duration-500">

    <div class="md:w-1/2 bg-blue-600/10 p-12 lg:p-16 flex flex-col justify-center border-r border-white/5">
      <p class="text-[10px] font-black text-blue-400 tracking-widest uppercase mb-4">University Gateway</p>
      <h2 class="text-4xl lg:text-5xl font-bold text-white mb-6 leading-tight">
        {isLogin ? "Your Next Discovery Starts Here." : "Join the Student Collective."}
      </h2>
      <p class="text-gray-400 text-sm lg:text-base leading-relaxed max-w-sm">
        {isLogin
          ? "Connect, share research, and discover insights from students across the globe."
          : "Create your account to start publishing your stories and engaging with university research."}
      </p>
    </div>

    <div class="md:w-1/2 relative p-10 lg:p-14 bg-black/40 overflow-hidden flex flex-col justify-center">
      <img
        src={bg}
        class="absolute inset-0 w-full h-full object-cover transition-transform duration-1000 {isLogin ? 'scale-100' : 'scale-110'}"
        alt=""
      />
      <div class="absolute inset-0 bg-black/70 backdrop-blur-sm"></div>

      <div class="relative z-10 flex flex-col h-full">
        <h3 class="text-2xl font-bold text-white mb-8">
          {isLogin ? "Sign In" : "Create Account"}
        </h3>

        {#if error}
          <div class="mb-4 px-4 py-3 rounded-xl bg-red-500/20 border border-red-500/30 text-red-400 text-sm">
            {error}
          </div>
        {/if}

        <div class="space-y-4 flex-grow">
          {#if !isLogin}
            <input
              type="text"
              bind:value={firstName}
              placeholder="First Name"
              class="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50 transition-all"
            />
          {/if}

          <input
            type="email"
            bind:value={email}
            placeholder="University Email"
            class="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50 transition-all"
          />

          <input
            type="password"
            bind:value={password}
            placeholder="Password"
            class="w-full bg-black/40 border border-white/10 rounded-xl px-4 py-3 text-sm text-white outline-none focus:ring-2 ring-blue-500/50 transition-all"
          />

          <button
            onclick={handleSubmit}
            disabled={loading}
            class="w-full bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white font-bold py-3.5 rounded-xl transition-colors mt-2 shadow-lg shadow-blue-900/20 active:scale-95"
          >
            {loading ? 'Please wait…' : (isLogin ? 'Continue' : 'Register Now')}
          </button>
        </div>

        <div class="mt-8 text-center">
          <p class="text-sm text-gray-400">
            {isLogin ? "Don't have an account?" : "Already have an account?"}
            <button
              onclick={toggleMode}
              class="text-blue-400 font-bold hover:text-blue-300 ml-1 transition-colors underline underline-offset-4"
            >
              {isLogin ? "Register" : "Log In"}
            </button>
          </p>
        </div>

      </div>
    </div>

  </div>
</section>

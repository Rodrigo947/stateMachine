export default {
  ssr: false,

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: 'State Machine - %s',
    title: 'Carregando',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.png' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@fortawesome/fontawesome-free/css/all.css', // https://fontawesome.com/v5.15/icons?d=gallery&p=2&q=house&m=free
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [{ src: '~/plugins/v-mask.js', mode: 'client' }],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxt/typescript-build', // https://go.nuxtjs.dev/typescript
    '@nuxtjs/vuetify', // https://go.nuxtjs.dev/vuetify
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios', // https://go.nuxtjs.dev/axios
    '@nuxtjs/auth-next', // https://auth.nuxtjs.org/status/
    '@nuxtjs/toast', // https://github.com/shakee93/vue-toasted
  ],

  auth: {
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'access',
        },
        refreshToken: {
          property: 'refresh',
          data: 'refresh',
        },
        user: {
          property: false,
          autoFetch: true,
        },
        endpoints: {
          login: { url: '/auth/token/', method: 'post' },
          refresh: { url: '/auth/token/refresh/', method: 'post' },
          user: { url: '/user/me/', method: 'get' },
          logout: false,
        },
      },
    },
    redirect: {
      login: '/login',
      logout: '/login',
      home: '/',
    },
  },

  router: {
    middleware: ['auth'],
  },

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    baseURL: `http://localhost:${process.env.DJANGO_DEV_PORT || '9005'}/api/`,
  },

  toast: {
    position: 'top-right',
    duration: 6000,
  },

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},

  server: {
    host: '0.0.0.0',
    port: process.env.VUE_PORT || 3000,
  },

  watchers: {
    webpack: {
      poll: true,
    },
  },
}

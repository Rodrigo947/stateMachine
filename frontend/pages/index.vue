<template>
  <div>
    <h1 class="mb-3">Olá {{ name }} {{ lastName }}</h1>

    <v-row>
      <v-col v-for="item in options" :key="item.name" cols="12" md="6">
        <NuxtLink :to="item.link" class="no-text-decoration">
          <v-card class="fill-height">
            <div class="d-flex flex-no-wrap justify-space-between">
              <div>
                <v-card-title class="word-break-word" v-text="item.name" />
              </div>
              <v-avatar class="ma-3 d-sm-flex" size="125" tile>
                <v-icon x-large>{{ item.icon }}</v-icon>
              </v-avatar>
            </div>
          </v-card>
        </NuxtLink>
      </v-col>

      <v-col cols="12" md="6">
        <v-card class="fill-height" @click="logout()">
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title class="word-break-none">Logout</v-card-title>
            </div>
            <v-avatar class="ma-3 d-sm-flex" size="125" tile>
              <v-icon x-large>fas fa-sign-out-alt</v-icon>
            </v-avatar>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  layout: 'default',
  data() {
    return {
      name: this.$auth.user.first_name,
      lastName: this.$auth.user.last_name,

      options: [
        {
          name: 'Perfil',
          icon: 'fas fa-user-edit',
          link: 'profile',
        },
        {
          name: 'Máquinas de Estado',
          icon: 'mdi-sitemap ',
          link: 'stateMachine',
        },
      ],
    }
  },
  head: {
    title: 'Página Inicial',
  },

  methods: {
    async logout() {
      await this.$auth.logout()
    },
  },
}
</script>

<style scoped>
.no-text-decoration {
  text-decoration: none;
}
.word-break-word {
  word-break: break-word;
}
</style>
<template>
  <v-app-bar app>
    <v-app-bar-nav-icon @click="toggleNav"></v-app-bar-nav-icon>

    <v-toolbar-title class="pl-0">
      <NuxtLink to="/">
        <v-img contain max-width="190" src="logo_header.png" />
      </NuxtLink>
    </v-toolbar-title>

    <v-spacer></v-spacer>

    <v-menu offset-y>
      <template #activator="{ on, attrs }">
        <v-chip
          class="ma-2"
          color="transparent"
          label
          large
          v-bind="attrs"
          v-on="on"
        >
          <span class="d-none d-sm-flex">{{ userEmail }}</span>
          <v-avatar size="38" right>
            <v-icon dark> mdi-account-circle </v-icon>
          </v-avatar>
        </v-chip>
      </template>
      <v-list>
        <v-list-item @click="logout()">
          <v-list-item-icon>
            <v-icon>fas fa-sign-out-alt</v-icon>
          </v-list-item-icon>
          <v-list-item-title>Logout</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  data() {
    return {
      userEmail: this.$auth.user.email,
    }
  },
  methods: {
    ...mapMutations({
      toggleNav: 'toggleNav',
    }),
    async logout() {
      await this.$auth.logout()
    },
  },
}
</script>


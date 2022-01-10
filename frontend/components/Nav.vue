<template>
  <v-navigation-drawer
    v-model="drawer"
    app
    temporary
    dark
    color="indigo darken-2"
  >
    <v-list-item class="white">
      <v-list-item-content>
        <v-list-item-title>
          <v-img contain src="logo_header.png" />
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    >
    <NuxtLink
      v-for="item in menu"
      :key="item.name"
      :to="item.link"
      :value="false"
      class="no-text-decoration"
    >
      <v-list-item>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>
            {{ item.name }}
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </NuxtLink>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {}
  },
  computed: {
    drawer: {
      get() {
        return this.$store.state.drawer
      },
      set(value) {
        this.$store.commit('updateDrawer', value)
      },
    },
    menu: {
      get() {
        return this.$store.state.menu
      },
    },
  },
}
</script>

<style scoped>
.no-text-decoration {
  text-decoration: none;
}
</style>

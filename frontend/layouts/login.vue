<template>
  <v-app>
    <v-app-bar max-height="58" class="d-md-none bg_ice_white">
      <v-img contain max-height="40" src="logo_header.png" />
    </v-app-bar>
    <v-main>
      <v-container class="ma-0 pa-0" fill-height fluid>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<style scoped>
html {
  overflow-y: hidden;
}

.bg_ice_white {
  background-color: #f6f7ff;
}
</style>

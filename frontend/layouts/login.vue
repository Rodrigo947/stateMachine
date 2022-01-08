<template>
  <v-app>
    <v-app-bar max-height="58" class="d-md-none bg_ice_white">
      <v-img contain max-height="40" src="#" />
    </v-app-bar>
    <v-main>
      <v-container class="ma-0 pa-0" fill-height fluid>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer app class="align-center justify-center d-flex bg-white">
      <v-img contain max-height="75" src="#" />
    </v-footer>
  </v-app>
</template>

<style scoped>
html {
  overflow-y: auto !important;
}
.bg-white {
  background-color: white !important;
}
.bg_ice_white {
  background-color: #f6f7ff !important;
}
</style>

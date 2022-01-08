<template>
  <v-row class="fill-height no-gutters">
    <v-col md="7" class="align-center justify-center d-none d-md-flex">
      <v-img max-height="325" max-width="440" src="#" />
    </v-col>
    <v-col xs="12" md="5" class="bg_ice_white">
      <v-row class="fill-height no-gutters">
        <v-col xs="12" class="align-center justify-center d-flex">
          <FormsLoginSignIn v-if="showFormSignIn" />
          <FormsLoginSignUp v-else />
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>


<script >
export default {
  layout: 'login',
  data: () => ({
    resetCode: false,
  }),
  head: {
    title: 'Bem Vindo',
  },
  computed: {
    showFormSignIn() {
      return this.$store.state.showFormSignIn
    },
  },
}
</script>

<style scoped>
.bg_ice_white {
  background-color: #f6f7ff;
}

.form {
  height: calc(100vh - 100px);
}
</style>

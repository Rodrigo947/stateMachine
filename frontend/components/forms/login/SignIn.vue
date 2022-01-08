<template>
  <div class="min-width-300">
    <form @submit.prevent="login">
      <h1 class="mb-3">Bem Vindo</h1>
      <v-text-field
        v-model="user.username"
        prepend-icon="mdi-account"
        label="E-mail, CPF ou PIS"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.password"
        label="Senha"
        required
        prepend-icon="mdi-lock"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :type="showPassword ? 'text' : 'password'"
        @click:append="showPassword = !showPassword"
      />
      <v-row>
        <v-col class="align-center d-flex">
          <v-btn plain @click="toggleShowFormSignIn">Cadastre-se</v-btn>
        </v-col>
        <v-col class="align-center justify-end d-flex">
          <v-btn
            type="submit"
            color="indigo darken-1 white--text"
            :loading="loading"
            :disabled="loading"
          >
            Login
          </v-btn>
        </v-col>
      </v-row>
    </form>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapMutations } from 'vuex'

export default Vue.extend({
  data: () => ({
    user: {
      username: '',
      password: '',
    },
    showPassword: false,
    loading: false,
  }),

  methods: {
    ...mapMutations({
      toggleShowFormSignIn: 'toggleShowFormSignIn',
    }),
  },
})
</script>


<style scoped>
.min-width-300 {
  min-width: 300px;
}
</style>
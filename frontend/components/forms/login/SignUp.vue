<template>
  <div class="min-width-300">
    <form @submit.prevent="login">
      <h1 class="mb-3">Cadastre-se</h1>

      <v-text-field
        v-model="user.first_name"
        :rules="rules.first_name"
        label="Nome"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.last_name"
        :rules="rules.last_name"
        label="Sobrenome"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.email"
        :rules="rules.email"
        label="E-mail"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.cpf"
        v-mask="'###.###.###-##'"
        :rules="rules.cpf"
        label="CPF"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.pis"
        v-mask="'###.#####.##-#'"
        :rules="rules.pis"
        label="PIS"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.password"
        label="Senha"
        :rules="rules.password"
        required
        prepend-icon="mdi-lock"
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :type="showPassword ? 'text' : 'password'"
        @click:append="showPassword = !showPassword"
      />

      <v-row>
        <v-col class="align-center d-flex">
          <v-btn plain @click="toggleShowFormSignIn">Cancelar</v-btn>
        </v-col>
        <v-col class="align-center justify-end d-flex">
          <v-btn
            type="submit"
            color="indigo darken-1 white--text"
            :loading="loading"
            :disabled="loading"
          >
            Registrar
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
      first_name: '',
      last_name: '',
      email: '',
      cpf: '',
      pis: '',
      password: '',
      repeat_password: '',
      pais: '',
      cep: '',
      estado: '',
      municipio: '',
      rua: '',
      numero: '',
      complemento: '',
    },
    rules: {
      first_name: [(v: string) => !!v || 'Nome é necessário'],
      last_name: [(v: string) => !!v || 'Sobrenome é necessário'],
      email: [
        (v: string) => !!v || 'E-mail é necessário',
        (v: string) => /.+@.+\..+/.test(v) || 'E-mail inválido',
      ],
      cpf: [(v: string) => !!v || 'CPF é necessário'],
      pis: [(v: string) => !!v || 'PIS é necessário'],
      password: [(v: string) => !!v || 'Senha é necessária'],
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
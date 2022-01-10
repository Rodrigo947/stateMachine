<template>
  <div class="min-width-300">
    <v-form ref="form" v-model="valid" lazy-validation>
      <h1 class="mb-3">Cadastre-se</h1>

      <v-text-field
        v-model="user.first_name"
        :rules="rules.first_name"
        label="Nome *"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.last_name"
        :rules="rules.last_name"
        label="Sobrenome *"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.email"
        :rules="rules.email"
        label="E-mail *"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.cpf"
        v-mask="'###.###.###-##'"
        :rules="rules.cpf"
        label="CPF *"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.pis"
        v-mask="'###.#####.##-#'"
        :rules="rules.pis"
        label="PIS *"
        required
      ></v-text-field>

      <v-text-field
        v-model="user.password"
        label="Senha *"
        :rules="rules.password"
        required
        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
        :type="showPassword ? 'text' : 'password'"
        @click:append="showPassword = !showPassword"
      />

      <v-row class="mt-3">
        <v-col class="align-center d-flex">
          <v-btn plain @click="toggleShowFormSignIn">Cancelar</v-btn>
        </v-col>
        <v-col class="align-center justify-end d-flex">
          <v-btn
            color="indigo darken-1 white--text"
            :loading="loading"
            :disabled="loading"
            @click="cadastrar"
          >
            Cadastrar
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import validarCPF from '../../../utils/validarCPF'
import validarPIS from '../../../utils/validarPIS'

export default {
  data: () => ({
    valid: true,
    user: {
      first_name: '',
      last_name: '',
      email: '',
      cpf: '',
      pis: '',
      password: '',
    },
    rules: {
      first_name: [(v) => !!v || 'Nome é necessário'],
      last_name: [(v) => !!v || 'Sobrenome é necessário'],
      email: [
        (v) => !!v || 'E-mail é necessário',
        (v) => /.+@.+\..+/.test(v) || 'E-mail inválido',
      ],
      cpf: [
        (v) => !!v || 'CPF é necessário',
        (v) => validarCPF(v) || 'CPF inválido',
      ],
      pis: [
        (v) => !!v || 'PIS é necessário',
        (v) => validarPIS(v) || 'PIS inválido',
      ],
      password: [(v) => !!v || 'Senha é necessária'],
    },
    showPassword: false,
    loading: false,
  }),

  methods: {
    ...mapMutations({
      toggleShowFormSignIn: 'toggleShowFormSignIn',
    }),

    async cadastrar() {
      if (this.$refs.form.validate()) {
        const userSend = {
          ...this.user,
          cpf: this.user.cpf.replace(/\./g, '').replace(/-/g, ''),
          pis: this.user.pis.replace(/\./g, '').replace(/-/g, ''),
        }

        await this.$axios
          .$post('signup/', userSend)
          .then(() => {
            this.toggleShowFormSignIn()
            this.$toast.success('Usuário criado')
          })
          .catch(() => {
            this.$toast.error('Dados Incorretos')
          })
      }
    },
  },
}
</script>


<style scoped>
.min-width-300 {
  min-width: 300px;
}
</style>
<template>
  <v-dialog
    v-model="dialogChangePassword"
    content-class="overflow-hidden"
    max-width="500px"
  >
    <template #activator="{ on, attrs }">
      <v-btn
        dark
        class="mb-2 indigo darken-2"
        v-bind="attrs"
        block
        max-width="100px"
        v-on="on"
      >
        <v-icon left small> mdi-lock </v-icon>
        Mudar senha
      </v-btn>
    </template>
    <v-card>
      <v-card-title class="d-flex justify-center">
        <span class="text-h5 text-center word-break"> Mudar Senha </span>
      </v-card-title>

      <v-card-text>
        <v-form ref="formChangePassword">
          <v-row>
            <v-col cols="12">
              <v-text-field
                v-model="password.old_password"
                label="Senha antiga"
                :append-icon="oldShowPassword ? 'mdi-eye' : 'mdi-eye-off'"
                :type="oldShowPassword ? 'text' : 'password'"
                :rules="rules_old_password"
                required
                @click:append="oldShowPassword = !oldShowPassword"
              ></v-text-field>
            </v-col>

            <v-col cols="12">
              <v-text-field
                v-model="password.new_password"
                label="Nova senha"
                :append-icon="newShowPassword ? 'mdi-eye' : 'mdi-eye-off'"
                :type="newShowPassword ? 'text' : 'password'"
                :rules="rules_new_password"
                required
                @click:append="newShowPassword = !newShowPassword"
              ></v-text-field>
            </v-col>
            <v-col cols="12">
              <v-text-field
                v-model="password.repeat_password"
                label="Repita a senha"
                :append-icon="repeatShowPassword ? 'mdi-eye' : 'mdi-eye-off'"
                :type="repeatShowPassword ? 'text' : 'password'"
                :rules="rules_repeat_password"
                required
                @click:append="repeatShowPassword = !repeatShowPassword"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-form>
      </v-card-text>

      <v-card-actions>
        <v-row>
          <v-col>
            <v-btn
              text
              color="red darken-1"
              :disabled="disabledBtn"
              block
              @click="cancelar()"
            >
              <v-icon left small> fas fa-ban </v-icon>
              Cancelar
            </v-btn>
          </v-col>
          <v-col>
            <v-btn
              text
              color="indigo darken-1"
              class="mr-2"
              :loading="loadingSave"
              :disabled="disabledBtn"
              block
              @click="mudarSenha()"
            >
              <v-icon left small> fas fa-check-circle </v-icon>
              Trocar senha
            </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      password: {
        old_password: '',
        new_password: '',
        repeat_password: '',
      },
      dialogChangePassword: false,
      oldShowPassword: false,
      newShowPassword: false,
      repeatShowPassword: false,
      disabledBtn: false,
      loadingSave: false,
    }
  },

  computed: {
    rules_old_password() {
      const rules = []

      rules.push((v) => !!v || 'Senha antiga é necessária')

      return rules
    },
    rules_new_password() {
      const rules = []

      rules.push((v) => !!v || 'Senha nova é necessária')

      rules.push(
        (v) =>
          (v || '').length >= 8 || 'Senha deve conter mais que 8 caracteres'
      )

      rules.push(
        (v) =>
          v !== this.password.old_password ||
          'A nova senha não pode ser igual a antiga'
      )

      return rules
    },
    rules_repeat_password() {
      const rules = []

      rules.push((v) => !!v || 'É necessário repetir a senha')

      rules.push((v) => {
        return v === this.password.new_password || 'As senhas não coincidem'
      })

      return rules
    },
  },

  methods: {
    async mudarSenha() {
      if (this.$refs.formChangePassword.validate()) {
        this.disabledBtn = true
        this.loadingSave = true
        await this.$axios
          .$post('user/change-password/', this.password)
          .then(() => {
            this.dialogChangePassword = false
            this.$refs.formChangePassword.reset()
            this.$toast.success('Senha Alterada')
          })
          .catch((err) => {
            this.$toast.error(err.response.data.message)
          })
          .finally(() => {
            this.disabledBtn = false
            this.loadingSave = false
          })
      }
    },
    cancelar() {
      this.dialogChangePassword = false
      this.$refs.formChangePassword.reset()
    },
  },
}
</script>

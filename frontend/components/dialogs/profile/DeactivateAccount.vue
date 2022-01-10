<template>
  <v-dialog
    v-model="dialogDeactivate"
    content-class="overflow-hidden"
    max-width="500px"
  >
    <template #activator="{ on, attrs }">
      <v-btn
        color="error"
        dark
        class="mb-2 indigo darken-2"
        v-bind="attrs"
        block
        v-on="on"
      >
        <v-icon left small> mdi-close </v-icon>
        Desativar Conta
      </v-btn>
    </template>
    <v-card>
      <v-card-title class="d-flex justify-center">
        <span class="text-h5 text-center word-break-word">
          Deseja realmente desativar sua conta?
        </span>
      </v-card-title>

      <v-card-actions>
        <v-row>
          <v-col>
            <v-btn
              text
              color="red darken-1"
              block
              @click="dialogDeactivate = false"
            >
              <v-icon left small> fas fa-ban </v-icon>
              Não
            </v-btn>
          </v-col>
          <v-col>
            <v-btn
              text
              color="indigo darken-1"
              class="mr-2"
              block
              @click="desativarConta"
            >
              <v-icon left small> fas fa-check-circle </v-icon>
              Sim
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
      dialogDeactivate: false,
    }
  },
  methods: {
    async desativarConta() {
      await this.$axios
        .$post('user/deactivate/', this.password)
        .then(() => {
          this.$auth.logout()
        })
        .catch((err) => {
          this.$toast.error(err.response.data.message)
        })
    },
  },
}
</script>

<style scoped>
.word-break-word {
  word-break: break-word;
}
</style>
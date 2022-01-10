<template>
  <div>
    <h3 class="mb-3 mt-3">Dados de acesso</h3>
    <v-row>
      <v-col cols="12" sm="12" md="6">
        <v-text-field v-model="email" label="E-mail" disabled></v-text-field>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" sm="6" md="3">
        <v-text-field
          v-model="cpf"
          v-mask="'###.###.###-##'"
          label="CPF"
          disabled
        ></v-text-field>
      </v-col>

      <v-col cols="12" sm="6" md="3">
        <v-text-field
          v-model="pis"
          v-mask="'###.#####.##-#'"
          label="PIS"
          disabled
        ></v-text-field>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" sm="6" md="3">
        <DialogsProfileChangePassword />
      </v-col>

      <v-col cols="12" sm="6" md="3">
        <DialogsProfileDeactivateAccount />
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: this.$auth.user.email,
      cpf: this.$auth.user.cpf,
      pis: this.$auth.user.pis,
    }
  },
}
</script>

<style>
</style>
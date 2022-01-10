<template>
  <div>
    <h3 class="mb-3">Informações Gerais</h3>
    <v-form ref="formInfo">
      <v-row>
        <v-col cols="12" sm="6" md="3">
          <v-text-field
            v-model="user.first_name"
            :rules="rules.first_name"
            label="Nome"
          ></v-text-field>
        </v-col>

        <v-col cols="12" sm="6" md="3">
          <v-text-field
            v-model="user.last_name"
            :rules="rules.last_name"
            label="Sobrenome"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="6" md="3">
          <v-select
            v-model="user.pais"
            :items="paises"
            item-text="nome.abreviado"
            item-value="nome.abreviado"
            label="País"
          ></v-select>
        </v-col>

        <v-col cols="12" sm="6" md="3">
          <v-text-field
            v-model="user.cep"
            v-mask="'#####-###'"
            label="CEP"
            @keyup="getInfoCEP()"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="6" md="3">
          <v-text-field
            v-model="user.estado"
            :rules="rules.estado"
            label="Estado"
          ></v-text-field>
        </v-col>

        <v-col cols="12" sm="6" md="3">
          <v-text-field
            v-model="user.municipio"
            label="Município"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="12" md="6">
          <v-text-field v-model="user.rua" label="Rua"></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="6" md="3">
          <v-text-field v-model="user.numero" label="Número"></v-text-field>
        </v-col>

        <v-col cols="12" sm="6" md="3">
          <v-text-field
            v-model="user.complemento"
            label="Complemento"
          ></v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" md="6" class="d-flex justify-end">
          <v-btn
            dark
            right
            class="mb-2 indigo darken-2"
            block
            @click="salvar()"
          >
            <v-icon left small> mdi-content-save </v-icon>Salvar</v-btn
          >
        </v-col>
      </v-row>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        ...this.$auth.user,
      },
      paises: [],
      rules: {
        first_name: [(v) => !!v || 'Nome é necessário'],
        last_name: [(v) => !!v || 'Sobrenome é necessário'],
        estado: [
          (v) =>
            v === '' ||
            /^[A-Z]{2}$/.test(v) ||
            'Estado deve conter apenas duas letras maiúsculas',
        ],
      },
    }
  },

  mounted() {
    this.getPaises()
  },

  methods: {
    async getPaises() {
      this.paises = await this.$axios.$get(
        'https://servicodados.ibge.gov.br/api/v1/paises/'
      )
      this.paises.sort(
        (a, b) =>
          (a.nome.abreviado > b.nome.abreviado) -
          (a.nome.abreviado < b.nome.abreviado)
      )
    },

    async getInfoCEP() {
      const formatCPF = this.user.cep.replace(/-/g, '')

      if (formatCPF.length === 8) {
        const axios = this.$axios.create()

        delete axios.defaults.headers.common.Authorization

        await axios
          .$get(`https://viacep.com.br/ws/${formatCPF}/json/`)
          .then((response) => {
            this.user.estado = response.uf
            this.user.municipio = response.localidade
            this.user.rua = response.logradouro
          })
      }
    },

    async salvar() {
      if (this.$refs.formInfo.validate()) {
        const userSend = {
          ...this.user,
          cep: this.user.cep.replace(/-/g, ''),
        }
        await this.$axios
          .$post('user/edit/', userSend)
          .then(() => {
            this.$toast.success('Dados atualizados')
          })
          .catch(() => {
            this.$toast.error('Dados Incorretos')
          })
      }
    },
  },
}
</script>

<style>
</style>
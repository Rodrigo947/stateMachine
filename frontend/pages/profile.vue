<template>
  <div>
    <h1>Perfil</h1>
    <FormsProfileAuth />
    <v-divider class="mb-3 mt-3"></v-divider>
    <FormsProfileGeneralInfo />
  </div>
</template>

<script>
export default {
  layout: 'default',
  head: {
    title: 'Perfil',
  },
}
</script>



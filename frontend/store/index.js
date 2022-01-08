export const state = () => ({
  drawer: false,
  showFormSignIn: true,
})

export const mutations = {
  toggleNav(state) {
    state.drawer = !state.drawer
  },
  updateDrawer(state, value) {
    state.drawer = value
  },

  toggleShowFormSignIn(state) {
    state.showFormSignIn = !state.showFormSignIn
  },
}

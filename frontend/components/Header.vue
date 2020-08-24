<template>
    <v-app-bar
      dark
      app
    >
        <v-toolbar-title>
            <nuxt-link
                to="/"
                class="toolbar_title"
            >
                Taspy
            </nuxt-link>
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <TaskForm ref="taskForm"></TaskForm>
        <v-btn class="mx-2" fab small dark @click="openTaskForm">
            <v-icon>mdi-plus</v-icon>
        </v-btn>
    </v-app-bar>
</template>

<script>
export default {
    methods: {
        openTaskForm() {
            this.$refs.taskForm.showDialog = true
        }
    }
}
</script>

<style scoped>
  .v-application .toolbar_title {
    color: inherit;
    text-decoration: none;
  }
</style>

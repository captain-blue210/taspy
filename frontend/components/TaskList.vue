<template>
    <div>
        <div v-for="task in tasks" :key="task.id">
            <nuxt-link
                :to="{name: 'task-id', params: {id: task.id}}"
            >
                <v-card
                    class="my-4"
                >
                    <v-card-title>
                        {{task.name}}
                    </v-card-title>
                    <v-card-subtitle>
                        期限日：{{task.expiration_dm}}
                    </v-card-subtitle>
                </v-card>
            </nuxt-link>
        </div>
    </div>
</template>

<script>
export default {
    props: ["tasks"],
}
</script>

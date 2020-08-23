<template>
    <div>
        <div v-for="task in tasks" :key="task.id">
            <nuxt-link
                :to="{name: 'task-id', params: {id: task.id}}">
                {{task.name}}{{task.status}}
            </nuxt-link>
        </div>
    </div>
</template>

<script>
export default {
    props: ["tasks"],
}
</script>

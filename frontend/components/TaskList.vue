<template>
    <div>
        <p v-for="task in tasks" :key="task.id">
            {{task.name}}
            {{task.status}}
        </p>
    </div>
</template>

<script>
export default {
    props: ["tasks"],
}
</script>

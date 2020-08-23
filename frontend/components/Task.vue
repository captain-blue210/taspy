<template>
    <div>
        <p>{{task.name}}</p>
        <p>期限日：{{task.expiration_dm | formatDate}}</p>
        <p>作成日：{{task.created_at | formatDate}}</p>
        <p>更新日：{{task.updated_at | formatDate}}</p>
        <p>ステータス：{{task.status}}</p>
    </div>
</template>

<script>
export default {
    props: ["task"],
}
</script>

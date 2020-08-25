<template>
  <v-row justify="center">
    <v-col cols="12">
      <v-card>
        <v-card-text>
            <v-text-field
                v-model="task.name"
                label="タスク名"
                required
            >
            </v-text-field>
            <v-menu
                ref="menu"
                v-model="menu"
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                min-width="290px"
            >
                <template v-slot:activator="{ on, attrs }">
                <v-text-field
                    v-model="task.expiration_dm"
                    label="期限日"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                ></v-text-field>
                </template>
                <v-date-picker
                    v-model="task.expiration_dm"
                    locale="ja-jp"
                    no-title
                    scrollable
                    :day-format="date => new Date(date).getDate()"
                >
                <v-spacer></v-spacer>
                <v-btn text color="primary" @click="menu = false">Cancel</v-btn>
                <v-btn text color="primary" @click="$refs.menu.save(task.expiration_dm)">OK</v-btn>
                </v-date-picker>
            </v-menu>
            <v-select
                v-model="task.status"
                label="ステータス"
                :items="statusItems"
            >
            </v-select>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="submit">更新</v-btn>
            <v-btn color="error" @click="deleteTaask">削除</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import axios from '~/plugins/axios'

export default {
    data() {
        return {
            menu: false,
            statusItems: ['OPEN','IN PROGRESS','CLOSED']
        }
    },
    props: ["task"],
    methods: {
        submit: function(){
            axios
                .put('/api/task/'+this.task.id+'/',{
                    id: this.task.id,
                    name: this.task.name,
                    expiration_dm: this.task.expiration_dm,
                    status: this.task.status,
                })
                .then(res => {
                    this.task.name = res.data.task.name
                    this.expiration_dm = res.data.task.expiration_dm
                    this.status = res.data.task.status
                })
        },
        deleteTaask: function(){
            axios
                .delete('/api/task/'+this.task.id+'/',{
                    id: this.task.id,
                })
                .then(res => {
                    this.$router.push('/')
                })
        }
    }
}
</script>

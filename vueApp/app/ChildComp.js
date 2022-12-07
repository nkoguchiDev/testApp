export default {
    props: {
        msg: String,
    },
    emits: ["response"],
    created() {
        this.$emit("response", this.msg);
    },
    template: `
    <h2>{{this.msg}}</h2>
    `,
};

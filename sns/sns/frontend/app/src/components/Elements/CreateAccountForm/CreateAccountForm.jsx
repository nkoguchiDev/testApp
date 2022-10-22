import { TextField } from "@mui/material";

export const CreateAccountForm = () => (
    <div>
        <TextField id="email" label="Email" helperText="required" variant="standard" />
        <br />
        <TextField
            id="password"
            label="Password"
            helperText="required"
            variant="standard"
        />
        <br />
        <TextField
            id="display_name"
            label="display name"
            helperText="required"
            variant="standard"
        />
    </div>
);

import { Button } from "@mui/material";

export const RichButton = (props) => (
    <div>
        <Button variant="outlined" onClick={props.onClick}>
            {props.type}
        </Button>
    </div>
);

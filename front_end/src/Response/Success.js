import React from 'react'
import './Response.css'

const Success = (props) => {
    let success = ''
    console.log(props.value)
    if (props.value.data_models) {
        success = <div className="success" key={props.value.data_models}>{props.value.data_models} is a data model that's present within the system.</div>
    }
    if (props.value.field_error && props.value.data_models) {
        success = 
                  <div className="field_failure">
                  <span className="field-error" key={props.value.field_error}>{props.value.field_error} is present but an invalid field.</span>
                  {props.value.data_models} is a data model present within the system.
                  </div>
    }
    if (props.value.date_filter) {
        success = <div className="success" key={props.value.date_filter}>{props.value.date_filter} is a date filter that's present within the system.</div>
    }
    if (props.value.sourcetypes_filter) {
        success = <div className="success" key={props.value.sourcetypes_filter}>{props.value.sourcetypes_filter} is a sourcetype that's present within the system.</div>
    }
    if (props.value.filters) {
        let filter = []
        for (var key in props.value.filters) {
            filter.push(key)
        }
        success = filter.map(item =>
            <div className="success" key={item}>{item} is a valid filter.</div>
        )
    }
    return (
        <div className="space_box">
            {success}
        </div>
    )
}

export default Success
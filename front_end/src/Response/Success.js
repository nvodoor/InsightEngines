import React from 'react'
import './Response.css'

const Success = (props) => {
    let success = ''
    let notsuccess = ''
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
        let notfilter = []
        for (var key in props.value.filters) {
            if (props.value.filters[key] === false) {
                notfilter.push(key)
            } else {
                filter.push(key)
            }
        }
        success = filter.map(item =>
            <div className="success" key={item}>{item} is a valid filter.</div>
        )
        notsuccess = notfilter.map(item => 
            <div className="field_failure">{item} is a specifically stated invalid filter.</div>
        )
    }
    return (
        <div className="space_box">
            {success}
            {notsuccess}
        </div>
    )
}

export default Success
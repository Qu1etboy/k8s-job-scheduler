from kubernetes import client, config

if __name__ == "__main__":
    # load config from ~/.kube/config (local)
    config.load_kube_config()
    v1 = client.BatchV1Api()

    # create a job
    job = client.V1Job(
        metadata=client.V1ObjectMeta(name="sync-data-job"),
        spec=client.V1JobSpec(
            # delete the pod after 10 seconds
            ttl_seconds_after_finished=10,
            template=client.V1PodTemplateSpec(
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="sync-data-job",
                            image="qu1etboy/k8s-jobs-demo:latest",
                            command=["./sync-data-job"]
                        )
                    ],
                    restart_policy="Never"
                )
            ),
            backoff_limit=4
        )
    )

    # run the job
    resp = v1.create_namespaced_job(
        body=job,
        namespace="default"
    )

    print(v1.list_namespaced_job(namespace="default"))
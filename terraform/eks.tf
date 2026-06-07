module "eks" {

  source = "terraform-aws-modules/eks/aws"

  version = "~> 20.0"

  cluster_name = "${var.project_name}-eks"

  cluster_version = var.cluster_version

  vpc_id = module.vpc.vpc_id

  subnet_ids = module.vpc.private_subnets

  enable_cluster_creator_admin_permissions = true

  # ==================================================
  # EKS API PUBLIC ACCESS
  # ==================================================

  cluster_endpoint_public_access = true

  # OPTIONAL:
  # Restrict access only to your public IP
  # Replace with your actual public IP

  # cluster_endpoint_public_access_cidrs = [
  #   "YOUR_PUBLIC_IP/32"
  # ]

  eks_managed_node_groups = {

    worker = {

      instance_types = [
        "t3.medium"
      ]

      min_size = 2

      max_size = 4

      desired_size = 2

      capacity_type = "ON_DEMAND"
    }
  }

  tags = local.common_tags
}